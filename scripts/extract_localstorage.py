"""Extract alumni-perfil-* and alumni-form-* values from Chrome leveldb localStorage.

Parses LDB table format directly:
  - Footer at end of file (48 bytes): metaindex BlockHandle, index BlockHandle, magic.
  - Index block lists all data blocks via BlockHandles.
  - Each block on disk: block_contents | 1-byte compression | 4-byte crc.
  - Data blocks may be Snappy-compressed (compression type 1).
  - Inside data block: entries with prefix-compressed keys.

Chrome localStorage encoding:
  Key   = b"_<origin>\\x00\\x01<keyname>" (e.g. b"_https://example.com\\x00\\x01alumni-perfil-foo")
  Value = 1-byte type (0=latin-1, 1=utf-16-le) + payload

Also reads .log files: append-only records (WAL). Each record has a header
(checksum 4 bytes, length 2 bytes, type 1 byte) then payload. The payload
itself is a batch of write operations.
"""
import os, re, json, sys, struct, io
import cramjam

LDB_DIR = r"C:\Users\gilberto.lucheti\chrome_ldb_copy"
OUT_DIR = r"C:\Users\gilberto.lucheti\alumni-plano-gerador\public\perfis"
ORIGIN = b"https://alumni-plano-gerador.vercel.app"
KEY_MARKER_PREFIX = b"_" + ORIGIN + b"\x00\x01"

os.makedirs(OUT_DIR, exist_ok=True)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

# ---------- varint ----------
def read_varint(buf, pos):
    result = 0
    shift = 0
    while True:
        b = buf[pos]
        pos += 1
        result |= (b & 0x7F) << shift
        if (b & 0x80) == 0:
            break
        shift += 7
    return result, pos

# ---------- BlockHandle ----------
def read_block_handle(buf, pos):
    offset, pos = read_varint(buf, pos)
    size, pos = read_varint(buf, pos)
    return (offset, size), pos

# ---------- Footer ----------
LEVELDB_MAGIC = 0xDB4775248B80FB57
FOOTER_SIZE = 48

def read_footer(file_bytes):
    if len(file_bytes) < FOOTER_SIZE:
        return None
    footer = file_bytes[-FOOTER_SIZE:]
    magic = struct.unpack("<Q", footer[-8:])[0]
    if magic != LEVELDB_MAGIC:
        return None
    pos = 0
    metaindex_h, pos = read_block_handle(footer, pos)
    index_h, pos = read_block_handle(footer, pos)
    return metaindex_h, index_h

def read_block(file_bytes, handle):
    offset, size = handle
    block = file_bytes[offset : offset + size]
    # trailer follows: 1 byte compression, 4 bytes crc
    compression = file_bytes[offset + size]
    if compression == 0:
        return block
    if compression == 1:
        # snappy (raw, not framed)
        return bytes(cramjam.snappy.decompress_raw(block))
    if compression == 2:
        return bytes(cramjam.zstd.decompress(block))
    if compression == 3:
        import zlib
        return zlib.decompress(block)
    raise ValueError(f"unknown compression {compression}")

def parse_data_block(block):
    """Yield (key_bytes, value_bytes) from a leveldb data block."""
    if len(block) < 4:
        return
    num_restarts = struct.unpack("<I", block[-4:])[0]
    restart_array_size = num_restarts * 4 + 4
    body = block[: -restart_array_size]

    pos = 0
    last_key = b""
    while pos < len(body):
        shared, pos = read_varint(body, pos)
        unshared, pos = read_varint(body, pos)
        value_len, pos = read_varint(body, pos)
        if shared == 0 and unshared == 0 and value_len == 0:
            break
        key_part = body[pos : pos + unshared]
        pos += unshared
        value = body[pos : pos + value_len]
        pos += value_len
        key = last_key[:shared] + key_part
        last_key = key
        yield key, value

def parse_index_block(block):
    """Index entries' values are BlockHandles."""
    for key, value in parse_data_block(block):
        # value is varint(offset) + varint(size)
        (offset, _), _ = (read_block_handle(value, 0))
        size, _ = read_varint(value, 0)  # not used; we re-decode
        # Properly re-decode:
        offset, p1 = read_varint(value, 0)
        size, _ = read_varint(value, p1)
        yield key, (offset, size)

def parse_ldb(file_bytes):
    """Yield (key, value) from all data blocks in an LDB file."""
    f = read_footer(file_bytes)
    if not f:
        return
    metaindex_h, index_h = f
    index_block = read_block(file_bytes, index_h)
    # Internal leveldb keys have an 8-byte trailer: [seq:7|type:1]
    # We strip these last 8 bytes from each key.
    for _ikey, handle in parse_index_block(index_block):
        try:
            data_block = read_block(file_bytes, handle)
        except Exception as e:
            print(f"  skip block {handle}: {e}", file=sys.stderr)
            continue
        for key, value in parse_data_block(data_block):
            # Strip 8-byte internal key trailer (seq + type)
            if len(key) >= 8:
                user_key = key[:-8]
            else:
                user_key = key
            yield user_key, value

# ---------- LOG files (write-ahead) ----------
# leveldb log block size = 32768
LOG_BLOCK_SIZE = 32768
# record types: 1=full, 2=first, 3=middle, 4=last
def parse_log(file_bytes):
    """Yield WriteBatch payload bytes from a log file."""
    pos = 0
    n = len(file_bytes)
    pending = bytearray()
    while pos < n:
        # block alignment
        space_left = LOG_BLOCK_SIZE - (pos % LOG_BLOCK_SIZE)
        if space_left < 7:
            pos += space_left
            continue
        if pos + 7 > n:
            break
        crc, length, rtype = struct.unpack("<IHB", file_bytes[pos : pos + 7])
        pos += 7
        if length == 0 and rtype == 0:
            break
        payload = file_bytes[pos : pos + length]
        pos += length
        if rtype == 1:  # full
            yield bytes(payload)
        elif rtype == 2:  # first
            pending = bytearray(payload)
        elif rtype == 3:  # middle
            pending.extend(payload)
        elif rtype == 4:  # last
            pending.extend(payload)
            yield bytes(pending)
            pending = bytearray()

def parse_writebatch(payload):
    """leveldb WriteBatch payload format:
      [seq:8][count:4] then `count` records:
        type:1 byte (0=del, 1=put)
        if put: key_len(varint) key value_len(varint) value
        if del: key_len(varint) key
    Yields (op, key, value)
    """
    if len(payload) < 12:
        return
    pos = 12
    n = len(payload)
    while pos < n:
        op = payload[pos]
        pos += 1
        if op == 1:  # put
            klen, pos = read_varint(payload, pos)
            key = payload[pos : pos + klen]
            pos += klen
            vlen, pos = read_varint(payload, pos)
            value = payload[pos : pos + vlen]
            pos += vlen
            yield "put", key, value
        elif op == 0:  # del
            klen, pos = read_varint(payload, pos)
            key = payload[pos : pos + klen]
            pos += klen
            yield "del", key, b""
        else:
            break

# ---------- Decode value ----------
def decode_value(value: bytes):
    """Chrome/Chromium localStorage value format:
        byte 0: encoding flag (0 = UTF-16 LE, 1 = Latin-1)
        rest:   payload in that encoding
    """
    if not value:
        return None
    t = value[0]
    body = value[1:]
    if t == 0:
        try:
            return body.decode("utf-16-le")
        except Exception:
            return None
    if t == 1:
        try:
            return body.decode("iso-8859-1")
        except Exception:
            return None
    return None

# ---------- Main ----------
results: dict[str, str] = {}

# Latest write wins; .ldb files first (sorted by name, lower numbers first), then .log (newest)
ldb_files = sorted(f for f in os.listdir(LDB_DIR) if f.endswith(".ldb"))
log_files = sorted(f for f in os.listdir(LDB_DIR) if f.endswith(".log"))

def process_kv(key_bytes: bytes, value_bytes: bytes, op: str = "put"):
    if not key_bytes.startswith(KEY_MARKER_PREFIX):
        return
    ls_key = key_bytes[len(KEY_MARKER_PREFIX):].decode("latin-1")
    if op == "del":
        results.pop(ls_key, None)
        return
    decoded = decode_value(value_bytes)
    if decoded is not None:
        results[ls_key] = decoded

for f in ldb_files:
    path = os.path.join(LDB_DIR, f)
    print(f"[ldb] {path}", file=sys.stderr)
    with open(path, "rb") as fh:
        blob = fh.read()
    count = 0
    for key, value in parse_ldb(blob):
        process_kv(key, value)
        count += 1
    print(f"   entries: {count}", file=sys.stderr)

for f in log_files:
    path = os.path.join(LDB_DIR, f)
    print(f"[log] {path}", file=sys.stderr)
    with open(path, "rb") as fh:
        blob = fh.read()
    batches = 0
    ops = 0
    for payload in parse_log(blob):
        batches += 1
        for op, key, value in parse_writebatch(payload):
            process_kv(key, value, op)
            ops += 1
    print(f"   batches: {batches}, ops: {ops}", file=sys.stderr)

print(f"\n[done] {len(results)} alumni keys for origin {ORIGIN.decode()}", file=sys.stderr)

perfis = {}
forms = {}
others = {}
for k, v in results.items():
    if k.startswith("alumni-perfil-"):
        perfis[k[len("alumni-perfil-"):]] = v
    elif k.startswith("alumni-form-"):
        forms[k[len("alumni-form-"):]] = v
    else:
        others[k] = v

print(f"  perfis: {len(perfis)}", file=sys.stderr)
for s in sorted(perfis): print(f"    {s}  ({len(perfis[s])} chars)")
print(f"  forms: {len(forms)}", file=sys.stderr)
for s in sorted(forms): print(f"    {s}  ({len(forms[s])} chars)")
if others:
    print(f"  outros (não perfil/form): {len(others)}", file=sys.stderr)
    for s in sorted(others): print(f"    {s}  ({len(others[s])} chars)")

# Write per-slug files merging perfil + form
slugs = set(perfis) | set(forms)
written = []
for slug in sorted(slugs):
    out_path = os.path.join(OUT_DIR, f"{slug}.json")
    payload = {}
    if slug in perfis:
        try: payload["perfil"] = json.loads(perfis[slug])
        except: payload["perfil_raw"] = perfis[slug]
    if slug in forms:
        try: payload["form"] = json.loads(forms[slug])
        except: payload["form_raw"] = forms[slug]
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    written.append(slug)

print(f"\n[written] {len(written)} per-slug files in {OUT_DIR}", file=sys.stderr)
