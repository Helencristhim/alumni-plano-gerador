# Padroes de UX e Design — Alumni by Better

> Documento de referencia para todas as interfaces Alumni.
> Referenciado por: `design-system.css`, todos os componentes

---

## Visao Geral

Este documento define os padroes obrigatorios de UX, acessibilidade,
performance e identidade visual para todos os produtos Alumni by Better.
Qualquer componente, pagina ou material gerado deve seguir estas regras.

---

## Acessibilidade (WCAG AA)

### Contraste

- Texto normal: ratio minimo de 4.5:1 contra o fundo
- Texto grande (18px+ bold ou 24px+ regular): ratio minimo de 3:1
- Elementos interativos: ratio minimo de 3:1 contra fundo adjacente
- Ferramenta de verificacao: usar WebAIM Contrast Checker

### Touch Targets

- Tamanho minimo de area tocavel: 44px x 44px
- Espacamento minimo entre alvos tocaveis: 8px
- Botoes de acao principal: minimo 48px de altura
- Links em texto corrido: padding vertical de pelo menos 4px

### Focus States

- Todo elemento interativo deve ter focus state visivel
- Estilo de focus: outline de 2px solid com offset de 2px
- Cor do outline: `#003080` (navy Alumni) em fundo claro
- Cor do outline: `#ffffff` em fundo escuro
- Nunca remover `outline` sem substituir por alternativa visivel
- Ordem de tab logica, seguindo fluxo visual da pagina

### Preferencias do Usuario

- `prefers-reduced-motion: reduce` — desabilitar animacoes, transicoes suaves
- `prefers-color-scheme` — respeitar quando implementado (futuro)
- `prefers-contrast: more` — aumentar contraste de bordas e texto secundario

### Formularios

- Todo input deve ter `<label>` associado via `htmlFor`/`id`
- Mensagens de erro devem usar `role="alert"` e `aria-live="polite"`
- Campos obrigatorios marcados com `aria-required="true"`
- Grupos de radio/checkbox encapsulados em `<fieldset>` com `<legend>`
- Placeholders nunca substituem labels

### Imagens e Midia

- Toda `<img>` deve ter `alt` descritivo (nunca vazio para conteudo)
- Imagens decorativas: `alt=""` e `aria-hidden="true"`
- Audio: sempre com controles visiveis e transcricao disponivel
- Video: legendas obrigatorias quando houver fala

---

## Performance

### Fontes

- `font-display: swap` em todas as declaracoes `@font-face`
- Preload das fontes criticas (Montserrat 400, 600; Cormorant Garamond 700)
- Subsets limitados ao necessario (latin, latin-ext)
- Formatos: woff2 prioritario, woff como fallback

### Carregamento de Imagens

- `loading="lazy"` em todas as imagens abaixo do fold
- `loading="eager"` apenas para imagens no viewport inicial
- Dimensoes `width` e `height` declaradas para evitar layout shift
- Formatos modernos: WebP com fallback para PNG/JPG

### Loading States

- Skeleton screens para conteudo que demora mais que 200ms
- Skeleton deve espelhar o layout final (mesmas proporcoes)
- Spinner apenas para acoes pontuais (salvar, enviar)
- Texto de loading: `"Carregando..."` (nunca so spinner sem texto)
- Progressbar para operacoes longas (geracao de plano, audio)

---

## Estados Visuais

Todo componente interativo deve implementar os 6 estados:

### Hover

- Transicao: 150ms ease-out
- Cor de fundo: escurece 8-12% ou aplica overlay sutil
- Cursor: `pointer` para elementos clicaveis
- Nao depender apenas de hover (mobile nao tem)

### Focus

- Outline: 2px solid `#003080` com offset de 2px
- Background: leve highlight (5% opacity do navy)
- Ativado por teclado (Tab) e assistive technology
- Visualmente distinto de hover

### Active (pressed)

- Transicao: imediata (0ms)
- Transform: `scale(0.97)` para botoes
- Background: escurece 15-20%
- Duracao perceptivel mas breve

### Disabled

- Opacidade: 0.5
- Cursor: `not-allowed`
- Sem hover, focus ou active states
- `aria-disabled="true"` (preferivel a atributo `disabled` quando possivel)
- Tooltip explicando por que esta desabilitado (quando relevante)

### Loading

- Spinner ou skeleton no lugar do conteudo
- Botao: texto substituido por spinner, largura mantida
- `aria-busy="true"` no container
- Interacao bloqueada (nao aceita cliques)

### Empty

- Mensagem amigavel explicando o estado vazio
- Ilustracao ou icone sutil (nunca pagina em branco)
- Call-to-action quando aplicavel
- Exemplo: `"Nenhum plano gerado ainda. Comece criando uma consultoria."`

---

## Microinteracoes

### Principios

- Duracao: 150-300ms para transicoes de interface
- Easing: `ease-out` para entrada, `ease-in` para saida
- Feedback imediato: usuario vê resposta em menos de 100ms
- Nunca usar animacoes que bloqueiam interacao

### Padroes de feedback

| Acao             | Feedback                                      | Duracao |
|------------------|-----------------------------------------------|---------|
| Clique em botao  | Scale down + cor ativa                        | 100ms   |
| Salvar com sucesso | Toast verde no topo                         | 3000ms  |
| Erro             | Toast vermelho + shake no campo               | 300ms   |
| Copiar texto     | Tooltip "Copiado!" proximo ao botao           | 2000ms  |
| Hover em card    | Elevacao sutil (shadow) + leve translate Y    | 200ms   |
| Abrir modal      | Fade in + scale de 95% para 100%              | 250ms   |
| Fechar modal     | Fade out + scale de 100% para 95%             | 200ms   |
| Progresso        | Barra animada com ease-out                    | 300ms   |

---

## Identidade Visual Alumni by Better

### Logo

- Arquivo: logo Alumni by Better (azul sobre fundo claro)
- Uso: sempre com clearspace minimo de 16px ao redor
- Nunca distorcer, rotacionar, recolorir ou adicionar efeitos
- Versao white para fundos escuros

### Tema Claro (padrao)

- Fundo principal: `#f5f5f0` (off-white quente)
- Texto principal: `#2d2d3a` (grafite escuro, nunca preto puro)
- Fundo de cards: `#ffffff`
- Bordas sutis: `#e5e5e0`
- Texto secundario: `#6b6b76`

### Paleta de Cores

| Cor        | Hex       | Uso                                          |
|------------|-----------|----------------------------------------------|
| Navy       | `#003080` | Cor primaria, botoes, links, icones de acao  |
| Navy hover | `#002460` | Hover states do navy                         |
| Vermelho   | `#d70c0c` | Alertas, erros, badges urgentes              |
| Verde      | `#22c55e` | Sucesso, confirmacao, acerto                 |
| Amarelo    | `#eab308` | Avisos, atencao, em andamento                |
| Cinza      | `#6b6b76` | Texto secundario, placeholders               |

### Tipografia

| Elemento            | Fonte              | Peso | Tamanho       |
|---------------------|--------------------|------|---------------|
| Titulos (h1-h3)     | Cormorant Garamond | 700  | 28-40px       |
| Subtitulos (h4-h6)  | Montserrat         | 600  | 18-24px       |
| Corpo               | Montserrat         | 400  | 15-16px       |
| Labels              | Montserrat         | 500  | 13-14px       |
| Captions            | Montserrat         | 400  | 12-13px       |
| Botoes              | Montserrat         | 600  | 14-16px       |

- Line height: 1.5 para corpo, 1.2 para titulos
- Letter spacing: normal (nunca tracking excessivo)

### Iconografia

- Biblioteca: Lucide Icons (Lucide React)
- Tamanho padrao: 20px
- Stroke width: 2px
- Cor: herda do texto ou usa navy para icones de acao
- Nunca misturar bibliotecas de icones

### Regras de Conteudo

- **Zero emojis** em interfaces, emails, materiais
- **Acentuacao perfeita** em todo texto em portugues
- **Ingles americano** (color, not colour; organize, not organise)
- Tom: profissional mas acolhedor, nunca robotico
- Tratamento: "voce" (nunca "tu" ou "senhor/senhora")

---

## Material do Aluno vs Admin

### Material do Aluno (aulas, exercicios, planos)

- Padding: 32-48px nas laterais (nunca apertado)
- Cards: maiores, com mais respiro, sombra sutil
- Tipografia: tamanhos generosos (corpo 16px minimo)
- Audio: em destaque, botao grande e visivel
- Cores: mais quentes, mais acolhedoras
- Espacamento vertical: 24-32px entre secoes
- Mobile: padding minimo de 16px, cards full-width

### Interface Admin (dashboard, configuracoes)

- Padding: 16-24px (mais denso, mais informacao por tela)
- Cards: compactos, dados em tabela quando possivel
- Tipografia: tamanhos menores (corpo 14px)
- Audio: funcional, tamanho padrao
- Cores: mais neutras, foco em dados
- Espacamento vertical: 16-20px entre secoes
- Tabelas: linhas alternadas, sort, filtros

---

## Breakpoints Responsivos

| Breakpoint | Largura    | Uso                          |
|------------|------------|------------------------------|
| Mobile     | < 640px    | Layout de coluna unica       |
| Tablet     | 640-1024px | 2 colunas, sidebar collapsa  |
| Desktop    | > 1024px   | Layout completo, sidebar fixa|

- Mobile first: estilizar para mobile, adicionar para desktop
- Nunca esconder conteudo essencial em mobile
- Menus: hamburger em mobile, expandido em desktop

---

## Checklist de Implementacao

Antes de considerar qualquer componente pronto:

- [ ] Todos os 6 estados visuais implementados
- [ ] Focus state visivel e acessivel
- [ ] Touch targets minimo 44px
- [ ] Contraste WCAG AA verificado
- [ ] Funciona em mobile (testado em 375px)
- [ ] Loading state implementado
- [ ] Empty state implementado (quando aplicavel)
- [ ] Animacoes respeitam prefers-reduced-motion
- [ ] Textos em portugues com acentuacao correta
- [ ] Sem emojis
- [ ] Fontes com font-display swap
- [ ] Imagens com lazy loading e dimensoes declaradas
