> **Documento normativo importado do Drive — nao editar aqui.**
> Origem: `Anexo_P-A_Padrao_de_Producao_de_Audios_ElevenLabs.docx`
> Drive ID: `19WfmAGOzP1nD62dtXs88yozAZdVh6lRd`
> Modificado no Drive: 2026-08-20
> Reimportar: `python3 scripts/consultivo/docx_to_md.py <arquivo.docx> docs/consultivo/ANEXO-P-A-audios-elevenlabs.md`
> A fonte e o .docx. Divergencia entre este arquivo e o Drive se resolve reimportando, nunca editando o .md.

**ANEXO P-A**

## Padrão de Produção de Áudios com ElevenLabs

*Private Class Alumni Black · Pre-class e In-class · Produção oficial*

Versão 5.0 · 20 de agosto de 2026 · Uso interno

## Estatuto

Este anexo é a especificação operacional citada por P1, P2 e P3. Ele não define conteúdo pedagógico, quantidade de etapas ou posição fixa de slides. Aplica-se sempre que a saída pedagógica aprovada exigir áudio.

### Regra canônica

Na produção final, todo áudio criado automaticamente para o material oficial é gerado pela API da ElevenLabs no pipeline seguro, antes da publicação. O HTML final apenas reproduz arquivos aprovados. Web Speech API, speechSynthesis e SpeechSynthesisUtterance são proibidos no build oficial.

## 1. Modos e fronteiras

| **Modo** | **Fonte de áudio** | **Interface** | **Status** |
|---|---|---|---|
| Protótipo/validação | Síntese do navegador admitida | Um aviso de que as vozes são provisórias | Não publicável para uso oficial |
| Produção final | Arquivos gerados pela API da ElevenLabs | Sem aviso de provisoriedade | Publicável após QA e suíte P3 |

A API é executada no pipeline seguro, nunca no navegador.

Credenciais permanecem em secret manager ou variável protegida; não entram em prompts, código, arquivos distribuídos ou logs públicos.

Falha de mídia não autoriza fallback para síntese do navegador.

O anexo regula geração; P1 regula o player e a experiência de uso.

## 2. Unidade de controle e rastreabilidade

Cada arquivo possui uma entrada no manifesto de mídia. O manifesto é a fonte de rastreabilidade e deve conter:

| **Campo obrigatório** | **Função** |
|---|---|
| asset_id | Identificador técnico estável, sem dados pessoais |
| lesson_id e uso | Associação à aula e à função pedagógica |
| transcript_version e transcript_hash | Prova da versão textual que originou o áudio |
| category | palavra/expressão, frase-modelo, narração, monólogo ou diálogo |
| model_id e endpoint | Modelo e operação efetivamente usados |
| voice_id(s) e role(s) | Voz associada a cada papel |
| voice_settings | Parâmetros completos aplicados |
| file, duration e checksum | Arquivo final e integridade |
| qa_status, reviewer e date | Aprovação auditiva rastreável |

Qualquer alteração no transcript, modelo, Voice ID, parâmetros ou arquivo invalida a aprovação correspondente.

## 3. Categorias funcionais

| **Categoria** | **Endpoint preferencial** | **Direção de voz** | **Critério central** |
|---|---|---|---|
| Palavra ou expressão isolada | Text to Speech | Clara, neutra e estável | Percepção fonética; sem introdução pronunciada |
| Frase-modelo/pronúncia | Text to Speech | Natural e controlada | Ritmo imitável e inteligibilidade |
| Narração ou monólogo | Text to Speech | Compatível com gênero e contexto | Coesão, pausas e duração adequadas ao nível |
| Diálogo com múltiplas vozes | Text to Dialogue | Personagens distinguíveis e coerentes | Turnos naturais; um arquivo final por diálogo |

A categoria decorre da função pedagógica, não de um número fixo de stage ou slide.

## 4. Modelo, vozes e manifesto de implantação

Modelo de referência vigente: eleven_v3. Antes de cada implantação, o pipeline valida a disponibilidade do modelo, dos endpoints e de cada Voice ID na conta autorizada. Alterações do provedor exigem atualização deliberada deste anexo.

| **Papel de voz** | **Perfil esperado** | **Uso** |
|---|---|---|
| Narrador(a) principal | American English, claro, profissional e neutro | Vocabulário, instrução sonora, exemplos e pronúncia |
| Personagem corporativo | Natural, profissional, sem dramatização excessiva | Reuniões, apresentações, negociações e networking |
| Personagem casual | Natural, conversacional e apropriado à idade | Viagens, hotel, aeroporto e conversas cotidianas |

Os nomes comerciais de voz não substituem Voice IDs. Os IDs ficam em manifesto controlado e são validados antes da geração. É proibido usar o mesmo Voice ID para dois personagens que devam soar distintos, salvo decisão explícita registrada.

## 5. Pré-processamento do transcript

Preservar significado, variedade linguística e American English do conteúdo aprovado.

Expandir abreviações, símbolos, moedas e números somente quando necessário para a pronúncia correta.

Remover do texto enviado os nomes de personagem usados apenas como rótulo de turno.

Usar pontuação e recursos oficialmente suportados pelo modelo; não inserir SSML incompatível.

Audio tags são opcionais e contextuais; limitar seu uso e nunca misturar direção corporativa e casual sem intenção pedagógica.

Não acrescentar explicações, exemplos ou linguagem que não estejam no transcript aprovado.

## 6. Fluxo obrigatório de geração

1. Congelar o transcript e registrar sua versão.

2. Classificar o áudio pela função pedagógica.

3. Selecionar endpoint, modelo, voz e parâmetros no manifesto validado.

4. Pré-processar o texto sem alterar o conteúdo pedagógico.

5. Executar a chamada autenticada no pipeline seguro.

6. Salvar o arquivo definitivo e calcular checksum.

7. Validar duração, pronúncia, clareza, ritmo, ruído, cortes, respirações e coerência de personagem.

8. Registrar a aprovação auditiva e associar o arquivo ao player.

9. Gerar o build e executar as validações P2/P3 na fonte e no publicado.

## 7. Requisitos do arquivo e nomenclatura

Formato de entrega preferencial: MP3 compatível com os navegadores suportados; parâmetros finais definidos pelo pipeline autorizado.

Nome técnico: lesson{NN}_{uso}_{asset-id}.mp3, sem nome do aluno ou outra informação pessoal.

Diálogo multi-voz é entregue como um arquivo único quando gerado pelo endpoint de diálogo; não concatenar turnos manualmente quando o endpoint nativo for aplicável.

Versões lenta e normal são arquivos ou variantes declaradas no manifesto; não são obtidas alterando artificialmente a reprodução sem validação pedagógica.

## 8. QA auditivo e critérios por nível

Ouvir integralmente cada arquivo; não aprovar por metadados ou inspeção visual da forma de onda.

Confirmar ausência de corte inicial/final, silêncio excessivo, clique, ruído, respiração artificial ou pronúncia inadequada.

A velocidade é adequada ao objetivo e ao nível. A1/A2 priorizam clareza sem fala infantilizada; níveis superiores preservam naturalidade e pressão comunicativa quando previstas.

Em diálogos, personagens são distinguíveis, turnos seguem o script e prosódia não contradiz a situação.

Nomes próprios, siglas e termos técnicos recebem validação específica.

Arquivo reprovado é regenerado e recebe nova versão; não é corrigido apenas por instrução textual na interface.

## 9. Segurança e privacidade

Nunca expor API key, token, cabeçalho de autenticação ou segredo em HTML, JavaScript, prompts distribuídos, source maps ou relatórios.

Não enviar dados pessoais desnecessários à API. Scripts personalizados devem ser anonimizados quando a identidade não for parte pedagogicamente necessária e autorizada.

Não usar clonagem de voz sem autorização documentada e governança específica.

Suspeita de exposição de credencial bloqueia a publicação e exige revogação, rotação e nova validação.

## 10. Checklist de liberação

☐ Modo de entrega definido antes da geração.

☐ Produção final gerada pela API da ElevenLabs no pipeline seguro.

☐ Nenhuma síntese ou chamada autenticada no navegador.

☐ Manifesto completo e Voice IDs validados.

☐ Transcript, arquivo e player pertencem à mesma versão.

☐ QA auditivo realizado em todos os arquivos.

☐ Credenciais ausentes dos artefatos distribuídos.

☐ Fonte e build aprovados nas verificações P2 e P3.

## Precedência

Se este anexo divergir de uma decisão pedagógica do núcleo 00–06, prevalece o núcleo. Se divergir de P1–P3 sobre entrega, segurança ou validação de áudio, a divergência bloqueia a publicação até a harmonização. O anexo não autoriza contagem fixa de etapas, slides ou ocorrências de áudio.
