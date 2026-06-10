# Integracao ElevenLabs — Audio nos Materiais

> Documento de referencia para geracao e uso de audio nos materiais Alumni.
> Referenciado por: gerador de material

---

## Principio Fundamental

> TODO bloco de texto longo e TODA frase de vocabulario tem audio.

Nao existe material Alumni sem audio. O audio nao e opcional, nao e bonus,
nao e "nice to have". E parte integral da experiencia pedagogica.
O aluno precisa ouvir ingles correto desde o primeiro contato com o material.

---

## Configuracao Tecnica

### Voz

- **Nome:** Arthur
- **Sotaque:** Americano (General American)
- **Provedor:** ElevenLabs
- **Motivo da escolha:** Voz masculina clara, ritmo natural, boa articulacao,
  nao soa robotica, consistente entre geracoes

### API

- **Servico:** ElevenLabs Text-to-Speech API
- **Endpoint:** `https://api.elevenlabs.io/v1/text-to-speech/{voice_id}`
- **Autenticacao:** API key via header `xi-api-key`
- **Modelo:** `eleven_multilingual_v2` (suporta ingles e portugues)
- **Voz unica por interlocutor (REGRA 35)** — em dialogos/role-play/listening com 2+ falantes, cada falante DEVE ter uma voz DIFERENTE, mesmo do mesmo genero. Roster: masculinas arthur/josh; femininas ellen/rachel/domi/bella. Cada linha leva `data-speaker` + `data-voice` (chave do roster). Mesmo personagem = mesma voz na aula inteira. Duas pessoas com a mesma voz = BUG bloqueante.
- **Formato de saida:** MP3
- **Configuracoes de voz:**
  - Stability: 0.5 (equilibrio entre consistencia e naturalidade)
  - Similarity boost: 0.75 (fidelidade a voz original)
  - Style: 0.0 (neutro, sem exagero emocional)
  - Use speaker boost: true

### Estrategia de Geracao

- **Quando:** Audio e gerado durante a criacao do material (build time)
- **Nunca em runtime:** O aluno nunca espera geracao de audio ao vivo
- **Armazenamento:** Arquivos .mp3 salvos no storage do projeto
- **Reutilizacao:** Gera uma vez, reutiliza indefinidamente
- **Nomenclatura:** `{aula-id}_{secao}_{indice}.mp3`
  - Exemplo: `lesson-03_vocab_01.mp3`
  - Exemplo: `lesson-03_intro_00.mp3`
  - Exemplo: `lesson-03_pronunciation_02.mp3`

### Parametros de Audio

- **Formato:** MP3
- **Bitrate:** 128kbps (equilibrio entre qualidade e tamanho)
- **Sample rate:** 44100 Hz
- **Canais:** Mono (voz falada nao precisa de estereo)
- **Tamanho medio:** 30-80KB por frase (5-15 segundos)

---

## Pontos de Audio Obrigatorios por Aula

Cada aula gerada DEVE conter audio nos seguintes pontos:

### 1. Introducao

- Audio do paragrafo introdutorio completo
- Ritmo: moderado, acolhedor
- Duracao tipica: 15-30 segundos

### 2. Cada Palavra/Expressao de Vocabulario

- Audio da palavra ou expressao isolada
- Pronuncia clara, ritmo levemente mais lento que conversacao
- Pausa de 0.3s antes e depois da palavra
- Duracao tipica: 2-5 segundos cada

### 3. Frases de Exemplo do Vocabulario

- Audio de cada frase de exemplo que acompanha o vocabulario
- Ritmo natural de conversacao
- Duracao tipica: 5-10 segundos cada

### 4. Texto de Contexto

- Audio do texto completo de contexto (80-150 palavras)
- Ritmo natural, com pausas nos pontos e virgulas
- Duracao tipica: 30-60 segundos

### 5. Explicacao Gramatical

- Audio dos exemplos gramaticais (nao da explicacao em portugues)
- Frases modelo com enfase na estrutura sendo ensinada
- Duracao tipica: 5-10 segundos por exemplo

### 6. Wrap-up

- Audio da mensagem de encerramento
- Tom: encorajador, positivo
- Duracao tipica: 10-20 segundos

### 7. Frases de Pronuncia

- Audio modelo de cada frase do exercicio de pronuncia
- Ritmo levemente mais lento que natural (para o aluno perceber fonemas)
- Articulacao especialmente clara
- Duracao tipica: 3-8 segundos cada

---

## Botao "Ouvir" no UI

### Posicionamento

- Posicionado a esquerda do texto ou acima do bloco de audio
- Inline com o conteudo (nao flutuante, nao fixo)
- Alinhado verticalmente ao centro do texto que reproduz
- Margem direita: 8px do texto adjacente

### Aparencia

- **Cor:** Navy (`#003080`)
- **Icone:** `volume-2` da biblioteca Lucide
- **Tamanho do icone:** 20px
- **Area clicavel:** 44px x 44px (acessibilidade)
- **Borda:** nenhuma em estado default
- **Background:** transparente em default
- **Border radius:** 8px

### Estados do Botao

#### Idle (padrao)

- Icone: `volume-2` (Lucide)
- Cor: `#003080` (navy)
- Background: transparente
- Cursor: pointer

#### Loading (carregando audio)

- Icone: substituido por spinner (Lucide `loader-2` com animacao rotate)
- Cor: `#6b6b76` (cinza)
- Cursor: wait
- Interacao: bloqueada (nao aceita cliques)
- `aria-busy="true"`

#### Playing (reproduzindo)

- Icone: `pause` (Lucide)
- Cor: `#003080` (navy)
- Background: `rgba(0, 48, 128, 0.08)` (navy com 8% opacity)
- Indicador visual: onda sonora animada ao lado do icone (opcional)
- Clique: pausa o audio

#### Paused (pausado)

- Icone: `play` (Lucide)
- Cor: `#003080` (navy)
- Background: `rgba(0, 48, 128, 0.05)` (navy com 5% opacity)
- Clique: retoma o audio de onde parou

### Acessibilidade do Botao

- `aria-label="Ouvir pronuncia"` ou `aria-label="Play audio"`
- `role="button"`
- Ativavel por Enter e Space
- Focus state: outline 2px solid `#003080` com offset 2px
- Ao iniciar: `aria-label` muda para `"Pausar audio"`
- Ao finalizar: retorna para estado idle automaticamente

### Comportamento

- Apenas um audio toca por vez (clicar em outro pausa o anterior)
- Audio reseta ao final (proximo clique reproduz do inicio)
- Em mobile: area de toque de 44px garantida
- Nao inicia automaticamente (nunca autoplay)
- Volume: controlado pelo sistema operacional (nao custom slider)

---

## Fluxo de Geracao

```
1. Gerador de material cria conteudo textual da aula
2. Para cada ponto de audio obrigatorio:
   a. Extrai o texto a ser convertido
   b. Chama ElevenLabs API com texto + configuracoes
   c. Recebe arquivo MP3
   d. Salva com nomenclatura padrao
   e. Registra URL do audio no JSON da aula
3. Material final inclui texto + URLs de audio
4. Frontend carrega audios sob demanda (lazy)
```

---

## Tratamento de Erros

### Falha na API ElevenLabs

- Retry automatico: 3 tentativas com backoff exponencial (1s, 2s, 4s)
- Apos 3 falhas: marcar ponto de audio como pendente
- Nao bloquear geracao do material (material pode existir sem audio)
- Notificar admin para reprocessar audios pendentes

### Texto muito longo

- Limite da API: ~5000 caracteres por request
- Textos acima: dividir em paragrafos e gerar audios separados
- Frontend concatena reproducao dos trechos

### Caracteres especiais

- Remover markdown antes de enviar para API
- Manter pontuacao (ajuda na entonacao natural)
- Substituir abreviacoes por extenso quando ambiguas

---

## Custos e Limites

- Plano ElevenLabs: verificar cota mensal de caracteres
- Estimativa por aula: ~2000-3000 caracteres de audio
- Estimativa por plano completo (24 aulas): ~50.000-70.000 caracteres
- Monitorar uso via dashboard ElevenLabs
- Alerta quando atingir 80% da cota mensal

---

## Boas Praticas

1. **Nunca gerar audio de texto em portugues** — Audio e exclusivamente
   para conteudo em ingles (exceto microcopy bilingue quando necessario)
2. **Testar audio antes de publicar** — Ouvir pelo menos 3 amostras por aula
3. **Atribuicao por genero** — Arthur (sfJopaWaOtauCD3HKX6Q) para alunos masculinos e personagens masculinos. Ellen (BIvP0GN1cAtSRTxNHnWS) para alunas femininas e personagens femininos. Palavras soltas e exercicios do aluno = voz do genero do aluno. Dialogos = voz do genero do personagem. Frases gerais = alternar. NUNCA usar so uma voz em todo o material
4. **Nao editar audio manualmente** — Se precisar corrigir, regenerar via API
5. **Cache agressivo** — Configurar headers de cache longo para arquivos .mp3
6. **Prefetch inteligente** — Carregar audio da secao atual + proxima secao

---

## Referencias Tecnicas

- API Docs: https://docs.elevenlabs.io/api-reference/text-to-speech
- Voice ID Arthur: configurado nas variaveis de ambiente (`ELEVENLABS_VOICE_ID`)
- API Key: variavel de ambiente (`ELEVENLABS_API_KEY`)
- Storage: definido pela infraestrutura do projeto
- Frontend: componente `AudioButton` reutilizavel
