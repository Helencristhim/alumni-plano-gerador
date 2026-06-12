# Pipeline do MODELO (aluna modelo Helen Mendes)

> **REGRA 20**: toda aula nova nasce daqui. Layout/CSS/JS vêm SEMPRE do shell da
> aluna modelo (`public/professor/helen-mendes-aula1.html` e hubs `helen-mendes.html`);
> o conteúdo vem do perfil 360 do aluno. NUNCA gerar CSS/JS do zero e NUNCA
> corrigir bug de layout num aluno individual — bug de layout se corrige NO MODELO
> e a correção chega aos próximos via builder. **Aulas passadas não são tocadas**
> (retrofit é fase 2, sob demanda, com OK da Helen).

## Fluxo por aula

```
1. Autorar conteúdo (do perfil 360):   _build/{slug}-aula{N}/slides.html (+preclass.html...)
2. Configurar:                          _build/{slug}-aula{N}/config.json (schema no build_from_model.py)
3. Buildar:                             python3 _build/model/build_from_model.py _build/{slug}-aula{N}/config.json
4. Gerar áudio:                         ELEVENLABS_API_KEY=... python3 _build/model/gen_audio.py _build/{slug}-aula{N}/config.json
5. Validar (GATE, bloqueante):          python3 _build/model/validate_lesson.py public/professor/{slug}-aula{N}.html public/aluno/{slug}-aula{N}.html
6. Contraste computado (GATE):          python3 check_computed_contrast.py (headless; 0 ilegível obrigatório)
7. Hub: inserir _build/{slug}-aula{N}/hub_snippets.html no hub existente (modo "snippets")
   ou usar hub "new" no config (aluno novo, sem hub)
8. PR → merge → deploy automático via GitHub (NUNCA vercel --prod)
```

## O que o shell do modelo garante de graça

EXIT→exitSlideMode() · handler de Escape fora de `<script src>` · listening = MP3 único
com player completo (mpToggle/mpSeek/mpSkip/mpSpeed) · revealError dinâmico · prefixo de
áudio a{N}_/pc_ · contrast-guard.js · nav-bar flex dentro do slides-wrapper (fix e615c853)
· 3ª cor de diálogo `.guest` · bloco de contraste slide-dark dos diálogos.

## Vozes (voices.json)

Só **arthur** e **ellen** existem na conta ElevenLabs (REGRA 35 — Ash/Kristen NÃO existem).
Regras bloqueantes do validador:
- toda `dialogue-line` tem `data-voice`
- 1 voz consistente por personagem no arquivo inteiro
- personagens distintos no MESMO diálogo = vozes distintas
- diálogo com mais falantes que vozes disponíveis = ERRO (reescrever ou adicionar voz)
- cross-check: o MP3 de cada fala (audio_manifest.json) foi gerado com a voz do `data-voice`

## Exercício novo (nível/idade/tipo de aula diferente)

Um tipo de exercício que ainda não existe entra PRIMEIRO no modelo (HTML+JS+regra no
validador), valida, e só então é usado em aluna(o) real. O validador pega estrutura
quebrada: handler `onclick` sem função correspondente, `<div>` desbalanceado, wildcard
de contraste, `data-exercise`, áudio sem MP3.
