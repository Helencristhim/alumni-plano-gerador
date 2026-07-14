# Novo Aluno — Perfil 360 sem formulário

Gera o Perfil 360 de um aluno novo pela linha de comando, no lugar de preencher
o formulário de `/index.html` no navegador.

É o **mesmo caminho** do site: monta o payload dos 8 blocos e faz `POST` em
`/api/perfil-360` (produção), que chama o Claude, valida o schema e faz upsert
na tabela `perfis` do Supabase. O aluno aparece no dashboard como `rascunho`,
exatamente como se tivesse vindo do formulário.

## Por que roda contra produção

As chaves (`ANTHROPIC_API_KEY`, `SUPABASE_SERVICE_KEY`) vivem na Vercel, não na
sua máquina — e é melhor assim. O script local só empacota e envia; quem gera e
grava é a função que já está no ar.

Única chave necessária aqui: `ELEVENLABS_API_KEY`, e **só** se você mandar áudio
em vez de transcrição. Ela já está no seu `.env.local`:

```bash
set -a; . ./.env.local; set +a
```

## Uso

```bash
# 1. cria o JSON do aluno a partir do modelo
python3 _build/novo-aluno/novo_aluno.py --template > alunos/maria.json

# 2. preenche o JSON (ver campos abaixo) e valida sem gastar API
python3 _build/novo-aluno/novo_aluno.py alunos/maria.json --dry-run

# 3. gera de verdade (1-3 min por aluno)
python3 _build/novo-aluno/novo_aluno.py alunos/maria.json

# lote
python3 _build/novo-aluno/novo_aluno.py alunos/*.json
```

## O JSON do aluno

**Obrigatórios** (os mesmos com `*` no formulário):
`nome`, `idade`, `sexo`, `email`, `foco`, `numAulas`, `duracao`, `frequencia`,
`modalidadeAula`, `nivel` — mais `transcricao_arquivo` **ou** `audio_arquivo`.

**Opcionais**: `profissao`, `cidade`, `whatsapp`, `modalidadeTrabalho`,
`plataforma`, `horarios`, `existeEvento`/`tipoEvento`/`dataEvento`/`localEvento`,
`stake`, `vitoria`, `historicoIngles`, `tempoForaAula`, `estiloAprendizagem`,
`estruturaPreferida`, `lidaComErros`, `energiaPreferida`, `seriesFilmes`,
`musicasPodcasts`, `hobbies`, `resumoZoom`, `observacoesProfessor`.

**Deixar opcional em branco não é preguiça** — o prompt do `perfil-360` extrai
esses campos da própria transcrição. `foco: "100% Personalizado"` inclusive
_manda_ o Claude deduzir o foco da consultoria. Preencha à mão só o que você
sabe melhor do que a transcrição.

Campos de `<select>` são validados contra a lista exata do formulário. Um valor
fora da lista (ex: `duracao: "1 hora"`) **falha antes de chamar a API** — se
passasse, o Claude improvisaria e o perfil sairia torto em silêncio.

`sexo` não é burocracia: define a voz dos áudios do material (Feminino = Ellen,
Masculino = Arthur).

## Transcrição

- `transcricao_arquivo`: `.txt` (Plaud), `.vtt`/`.srt` (Zoom) ou `.md`.
  Legenda do Zoom é limpa automaticamente — timestamps, cues e falas repetidas
  saem; o nome de quem fala fica.
- `audio_arquivo`: transcreve via ElevenLabs Scribe com separação de falantes,
  e salva um `.txt` ao lado do áudio. Se precisar refazer o perfil depois, aponte
  para esse `.txt` e você não paga STT de novo.
- Abaixo de 200 palavras o script avisa: o perfil sai raso porque o Claude não
  tem de onde extrair.

## Saída

- Copia o perfil completo em `_build/_perfis-novos/{slug}.json`.
- **Confirma no Supabase** que a linha existe de verdade (não confia no 200 da
  API) e imprime nível, nº de aulas e status.
- Imprime o link de revisão: `…/perfil.html?id={slug}`.

O `{slug}` sai do nome pela mesma regra do servidor, então bate com o que o
dashboard e o material vão usar.

## Depois disso

O perfil nasce como `rascunho`. Revisar em `/perfil.html?id={slug}` continua
sendo trabalho humano — e a geração do material segue a REGRA 20 (uma aula por
vez, via builder, com os gates). Este script para no perfil, de propósito.
