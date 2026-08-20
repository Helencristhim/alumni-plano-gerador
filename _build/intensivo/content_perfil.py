# -*- coding: utf-8 -*-
"""Perfil, planejamento e o registro do ciclo. Portugues aqui e do PROFESSOR."""

ALUNO = {'nome': 'Rita', 'sobrenome': 'Rodrigues'}

CICLO = {
    'numero': 1, 'aulas': 6, 'nivel': 'A2+',
    'programa': 'Intensive',
    'rotulo': 'Aulas neste intensivo', 'rotuloAluno': 'Lessons in this intensive',
    'badge': 'Intensivo &middot; 6 aulas &middot; A2+',
    'badgeAluno': 'Intensive &middot; 6 lessons',
}

ARTEFATO = {'id': 'rita-rodrigues-intensivo'}

CABECALHO = {
    'subtitulo': ('Ingl&ecirc;s para a visita da Carestream &mdash; apresentar a empresa, explicar a pr&oacute;pria '
                  'fun&ccedil;&atilde;o e sustentar a intera&ccedil;&atilde;o em 31/08.'),
    'info': ['Corporate Management &middot; Imagem Healthcare Solutions', 'S&atilde;o Paulo, SP'],
}

# ---------------------------------------------------------------- aba Perfil
PERFIL_PROF = """
  <p class="eyebrow">Perfil da aluna</p>
  <h2 class="sec">Quem &eacute; a <span data-lf="aluno-primeiro-nome">Rita</span>, e o que ela precisa conseguir fazer</h2>
  <p class="prep-p">Aluna adulta e executiva. N&atilde;o est&aacute; come&ccedil;ando do zero: teve contato intermitente com
     cursos e j&aacute; participou pontualmente de reuni&otilde;es em ingl&ecirc;s. O que falta n&atilde;o &eacute;
     conhecimento de mundo &mdash; &eacute; <strong>acesso r&aacute;pido &agrave; l&iacute;ngua sob press&atilde;o</strong>.</p>
  <div class="brief">
    <dl>
      <dt>Cargo</dt><dd>Corporate Management &mdash; Diretoria de Gest&atilde;o Corporativa. Responde ao propriet&aacute;rio/CEO,
        integra o conselho e atua como camada facilitadora da gest&atilde;o.</dd>
      <dt>Escopo</dt><dd>Tecnologia, RH, projetos, qualidade, controladoria, marketing e processos de neg&oacute;cio.
        <strong>N&atilde;o</strong> &eacute; CEO, CFO, diretora comercial nem diretora de servi&ccedil;os.</dd>
      <dt>N&iacute;vel de trabalho</dt><dd>A2+ assim&eacute;trico. O receptivo e o conhecimento de mundo est&atilde;o acima
        da produ&ccedil;&atilde;o espont&acirc;nea.</dd>
      <dt>Necessidade imediata</dt><dd>Receber, em S&atilde;o Paulo, visitantes da Carestream vindos dos Estados Unidos:
        apresentar a empresa ou apoiar o CEO, responder d&uacute;vidas previs&iacute;veis e participar da intera&ccedil;&atilde;o informal.</dd>
      <dt>Uso do ingl&ecirc;s hoje</dt><dd>Compreende e responde quando tem tempo para estruturar. Perde continuidade com
        velocidade, sotaque, palavra desconhecida e risco comunicativo.</dd>
      <dt>Framework do intensivo</dt><dd><strong>ESP &mdash; English for Specific Purposes</strong>, na variante
        Personalized Real-World English. Todas as seis aulas usam o mesmo framework.</dd>
    </dl>
  </div>

  <h2 class="sec">Pontos fortes e riscos</h2>
  <div class="grid2">
    <div class="card"><h4>Pontos fortes</h4>
      <ul class="prep-list">
        <li>Conhecimento da empresa e reperto&oacute;rio executivo &mdash; ela sabe o conte&uacute;do; falta a l&iacute;ngua.</li>
        <li>Capacidade de organizar ideias e racioc&iacute;nio executivo r&aacute;pido em portugu&ecirc;s.</li>
        <li>Consci&ecirc;ncia das pr&oacute;prias dificuldades, sem nega&ccedil;&atilde;o nem excesso de defesa.</li>
        <li>Motiva&ccedil;&atilde;o alta e disponibilidade real para rotina intensiva.</li>
      </ul></div>
    <div class="card"><h4>Riscos a observar durante a aula</h4>
      <ul class="prep-list">
        <li>Sobrecarga e vergonha &mdash; o material pede <strong>uma</strong> produ&ccedil;&atilde;o principal por aula, n&atilde;o v&aacute;rias.</li>
        <li>Hipermonitoramento e acelera&ccedil;&atilde;o do pensamento sob press&atilde;o.</li>
        <li>Tentativa de traduzir ideias complexas do portugu&ecirc;s, que trava a frase no meio.</li>
        <li>Colapso quando uma palavra bloqueia a sequ&ecirc;ncia. &Eacute; o risco central: por isso a estrat&eacute;gia de
            reparo entra j&aacute; na aula 1, e n&atilde;o depois.</li>
      </ul></div>
  </div>

  <h2 class="sec">O que se espera ao final &mdash; e o que n&atilde;o se espera</h2>
  <p class="prep-p">At&eacute; 28/08 ela deve apresentar os blocos priorit&aacute;rios <strong>com slides e mapas de fala
     consult&aacute;veis</strong>, responder 3&ndash;4 perguntas essenciais por &aacute;rea e manter a intera&ccedil;&atilde;o
     quando n&atilde;o compreender ou n&atilde;o tiver a informa&ccedil;&atilde;o.</p>
  <p class="prep-p"><strong>N&atilde;o</strong> se espera apresenta&ccedil;&atilde;o longa de mem&oacute;ria, dom&iacute;nio
     aut&ocirc;nomo de todo o deck, sotaque nativo nem aus&ecirc;ncia de erro. O crit&eacute;rio &eacute; efic&aacute;cia
     comunicativa &mdash; continuidade, inteligibilidade, precis&atilde;o dos dados e gest&atilde;o da intera&ccedil;&atilde;o.</p>

  <h3 class="sub">Regra das tr&ecirc;s camadas</h3>
  <p class="prep-p">Nem tudo que aparece na tela &eacute; exig&ecirc;ncia produtiva. Cada item da aula est&aacute; marcado como
     <strong>Essential</strong> &mdash; ela produz; <strong>With support</strong> &mdash; ela consulta; ou
     <strong>Recognize</strong> &mdash; ela entende, confirma ou encaminha. Converter o deck inteiro em produ&ccedil;&atilde;o
     &eacute; o erro que esta marca&ccedil;&atilde;o existe para impedir.</p>

  <h3 class="sub">Confidencialidade</h3>
  <p class="prep-p">Receita, lucro l&iacute;quido e participa&ccedil;&atilde;o por parceiro entram <strong>a partir da aula 5</strong>
     e est&atilde;o autorizados para esta reuni&atilde;o. Confirme antes da aula 5. Receita recorrente e comiss&otilde;es
     <strong>n&atilde;o</strong> foram fornecidas: n&atilde;o s&atilde;o esquecimento dela, e a resposta correta &eacute; encaminhar.</p>
"""

PLANNING_ALUNO = """
  <p class="eyebrow">Your planning</p>
  <h2 class="sec">Your intensive &mdash; six lessons</h2>
  <p class="prep-p">Six lessons: the first on 20 August, and then every day from 24 to 28 August. The meeting is on
     <strong>31 August</strong>. Each lesson has three parts: something short to do before class, the lesson itself,
     and a short review after it.</p>
  <div class="tbl-wrap"><table class="data" style="min-width:560px">
    <thead><tr><th style="width:62px">Lesson</th><th style="width:210px">Topic</th><th>What you will do</th></tr></thead>
    <tbody>
      <tr><td>1 &middot; 20 Aug</td><td data-lf="topico1">&mdash;</td><td>Open the presentation: say what the company does, how long it has worked, and what you are responsible for.</td></tr>
      <tr><td>2 &middot; 24 Aug</td><td data-lf="topico2">&mdash;</td><td>Tell the story of the company in four moments, and explain how it is organized today.</td></tr>
      <tr><td>3 &middot; 25 Aug</td><td data-lf="topico3">&mdash;</td><td>Present the main categories and partners, with one or two examples.</td></tr>
      <tr><td>4 &middot; 26 Aug</td><td data-lf="topico4">&mdash;</td><td>Explain where the company operates and what the service team does.</td></tr>
      <tr><td>5 &middot; 27 Aug</td><td data-lf="topico5">&mdash;</td><td>Say the main message of each chart, and answer questions about growth and opportunities.</td></tr>
      <tr><td>6 &middot; 28 Aug</td><td data-lf="topico6">&mdash;</td><td>Present with your slides, answer questions, and practice what to say when you do not understand.</td></tr>
    </tbody>
  </table></div>

  <h3 class="sub">Three things to keep in mind</h3>
  <div class="brief"><dl>
    <dt>You will always have your slides and your speech map.</dt>
    <dd>You are not expected to present from memory, and consulting them is not a failure &mdash; on the day either.</dd>
    <dt>You do not need to present every slide yourself.</dt>
    <dd>You will practice what is yours to explain, what you can read from the screen, and what you can pass to the person responsible.</dd>
    <dt>Your lessons will respond to what you need most.</dt>
    <dd>We may adjust the sequence or spend more time on a specific area based on your progress. Your final meeting simulation remains scheduled for 28 August.</dd>
  </dl></div>
"""

SYLLABUS = """
  <p class="eyebrow">Planejamento do intensivo</p>
  <h2 class="sec">Seis aulas, uma reuni&atilde;o</h2>
  <p class="prep-p">Este intensivo prepara a <span data-lf="aluno-primeiro-nome">Rita</span> para apresentar a Imagem
     Healthcare Solutions e participar da intera&ccedil;&atilde;o com os visitantes da Carestream. O percurso organiza os
     conte&uacute;dos priorit&aacute;rios da apresenta&ccedil;&atilde;o institucional em seis aulas, culminando na
     simula&ccedil;&atilde;o da reuni&atilde;o em <strong>28/08</strong>. A reuni&atilde;o acontece em <strong>31/08</strong>.
     O objetivo &eacute; automatizar a linguagem reutiliz&aacute;vel de cada &aacute;rea &mdash;
     <strong>cobrir a apresenta&ccedil;&atilde;o inteira n&atilde;o &eacute; objetivo do m&oacute;dulo</strong>.</p>
  <div class="callout ok"><span class="callout-title">Planejamento adapt&aacute;vel</span>
     A sequ&ecirc;ncia prevista pode ser ajustada conforme o desempenho observado nas primeiras aulas e a
     confirma&ccedil;&atilde;o das condi&ccedil;&otilde;es da reuni&atilde;o. A simula&ccedil;&atilde;o final de 28/08 se preserva.</div>

  <h3 class="sub">Vis&atilde;o geral das seis aulas</h3>
  <div class="tbl-wrap"><table class="data" style="min-width:760px">
    <thead><tr><th style="width:48px">Aula</th><th style="width:66px">Data</th><th style="width:170px">Foco</th>
      <th style="width:260px">Linguagem principal</th><th>Produto central</th></tr></thead>
    <tbody>
      <tr><td>1</td><td>20/08</td><td>Company overview &amp; Rita&rsquo;s role</td>
        <td><em>We have been&hellip; for&hellip; / We represent&hellip; / We distribute&hellip; / We provide&hellip; / I am responsible for&hellip;</em></td>
        <td>Abertura funcional com apoio &mdash; empresa, tempo de mercado, tr&ecirc;s modelos, alcance e fun&ccedil;&atilde;o pr&oacute;pria.</td></tr>
      <tr><td>2</td><td>24/08</td><td>History, expertise &amp; organization</td>
        <td><em>We started as&hellip; / In [year], we&hellip; / This allowed us to&hellip; / Today we are organized into&hellip; / I oversee&hellip;</em></td>
        <td>Narrativa apoiada de quatro marcos at&eacute; a organiza&ccedil;&atilde;o de hoje, com o papel da Rita e os n&uacute;meros gerais.</td></tr>
      <tr><td>3</td><td>25/08</td><td>Commercial portfolio &amp; partners</td>
        <td><em>Our portfolio covers&hellip; / We represent&hellip; / This solution is used for&hellip; / Our technical team can provide more detail.</em></td>
        <td>Vis&atilde;o geral do portf&oacute;lio: categorias, parceiros e um exemplo por categoria.</td></tr>
      <tr><td>4</td><td>26/08</td><td>Commercial and service coverage</td>
        <td><em>Our headquarters is in&hellip; / We operate directly in&hellip; / Our service team includes&hellip; / I would need to confirm that detail.</em></td>
        <td>Explica&ccedil;&atilde;o da cobertura comercial e da capacidade de servi&ccedil;o, com um benef&iacute;cio operacional.</td></tr>
      <tr><td>5</td><td>27/08</td><td>Results, growth &amp; integrated Q&amp;A</td>
        <td><em>&hellip; accounts for&hellip; / It increased from&hellip; to&hellip; / One opportunity is&hellip; / We expect&hellip; / I would need to confirm&hellip;</em></td>
        <td>Mensagem principal por gr&aacute;fico priorit&aacute;rio, um n&uacute;mero, uma compara&ccedil;&atilde;o e duas oportunidades &mdash; com o que dizer quando o dado n&atilde;o se confirma.</td></tr>
      <tr><td>6</td><td>28/08</td><td>Full meeting simulation</td>
        <td><em>Could you repeat that? / If I understood correctly&hellip; / Let me check the slide. / [Name] can provide more detail.</em></td>
        <td>Apresenta&ccedil;&atilde;o funcional com apoio, Q&amp;A previs&iacute;vel e estrat&eacute;gias de reparo.</td></tr>
    </tbody>
  </table></div>

  <h3 class="sub">Arquitetura da progress&atilde;o</h3>
  <div class="brief"><dl>
    <dt>1 &middot; Preparar e diagnosticar (aulas 1&ndash;2)</dt>
    <dd>Construir a abertura da apresenta&ccedil;&atilde;o, confirmar as necessidades de apoio e conectar empresa,
        hist&oacute;ria, estrutura e fun&ccedil;&atilde;o da Rita.</dd>
    <dt>2 &middot; Construir por &aacute;rea (aulas 3&ndash;4)</dt>
    <dd>Preparar os blocos priorit&aacute;rios sobre portf&oacute;lio, parceiros, cobertura comercial e servi&ccedil;os.</dd>
    <dt>3 &middot; Integrar e simular (aulas 5&ndash;6)</dt>
    <dd>Trabalhar resultados e perspectivas, integrar o Q&amp;A e realizar a simula&ccedil;&atilde;o completa da reuni&atilde;o.</dd>
  </dl></div>

  <h3 class="sub">Regras que valem em toda aula</h3>
  <ul class="prep-list">
    <li>Slides e mapa de fala ficam com a aluna, inclusive na reuni&atilde;o. Consultar n&atilde;o &eacute; falha.</li>
    <li>Uma produ&ccedil;&atilde;o principal por aula. Se faltar tempo, corte extens&atilde;o &mdash; nunca a
        produ&ccedil;&atilde;o, o feedback ou o retask.</li>
    <li>Nenhum n&uacute;mero fora do deck. Encaminhar &eacute; a resposta certa, e conta como sucesso.</li>
    <li>A produ&ccedil;&atilde;o inicial (etapa 3) vem antes de qualquer modelo.</li>
    <li>Um ponto de melhoria por aula &mdash; o de maior impacto. Nunca uma lista.</li>
    <li>A aula 6 n&atilde;o introduz conte&uacute;do novo.</li>
  </ul>
"""

# ------------------------------------------------- cartao da aula: preparacao
_MARGEM = ('Os 5 minutos restantes da hora s&atilde;o <strong>margem operacional</strong>, n&atilde;o conte&uacute;do. '
           'Produ&ccedil;&atilde;o principal, feedback emergente e retask s&atilde;o protegidos: se faltar tempo, corte '
           'extens&atilde;o, nunca eles.')
_ANTES_FIXO = ['Prepare-se para registrar a produ&ccedil;&atilde;o inicial dela como ela a disser. &Eacute; o instrumento '
               'diagn&oacute;stico da aula &mdash; e da aula seguinte.',
               'O in-class <strong>n&atilde;o depende</strong> do pre-class. Se ela n&atilde;o fez, a aula corre igual.',
               'Nenhum material externo &eacute; necess&aacute;rio. O deck da empresa n&atilde;o precisa estar aberto.']

PREP = {
 1: {'objetivo': ('Abrir a apresenta&ccedil;&atilde;o, posicionar a empresa e explicar a pr&oacute;pria fun&ccedil;&atilde;o '
                  'numa vers&atilde;o curta, apoiada e compreens&iacute;vel.'),
     'produto': ('Uma abertura funcional que cumpra as <strong>cinco fun&ccedil;&otilde;es</strong>: apresentar brevemente a '
                 'empresa, dizer h&aacute; quanto tempo ela atua, explicar os tr&ecirc;s modelos, indicar o alcance e '
                 'apresentar a pr&oacute;pria fun&ccedil;&atilde;o. Com slide e mapa de fala dispon&iacute;veis, factualmente '
                 'correta e sustentada sem colapso. Costuma levar cerca de um minuto &mdash; refer&ecirc;ncia de '
                 'opera&ccedil;&atilde;o, n&atilde;o meta para a aluna.'),
     'criterio': ('As cinco fun&ccedil;&otilde;es chegam ao interlocutor, com continuidade, inteligibilidade e '
                  'precis&atilde;o dos dados. <strong>N&atilde;o</strong> corre&ccedil;&atilde;o total, produ&ccedil;&atilde;o '
                  'de mem&oacute;ria nem dura&ccedil;&atilde;o-alvo.'),
     'antes': ['Leia o que ela escreveu na atividade 6 do pre-class. &Eacute; a evid&ecirc;ncia mais barata de acesso '
               'lexical que voc&ecirc; ter&aacute; antes de ouvi-la falar.'] + _ANTES_FIXO,
     'observar': ['Quanto apoio ela realmente usa &mdash; e o que acontece quando ele sai.',
                  'Continuidade: ela recupera depois de travar, ou a frase morre?',
                  'Inteligibilidade e velocidade de acesso ao vocabul&aacute;rio.',
                  'Compreens&atilde;o sem tradu&ccedil;&atilde;o para o portugu&ecirc;s.',
                  'Precis&atilde;o factual: 38 anos, os tr&ecirc;s modelos, o nome da pr&oacute;pria &aacute;rea.',
                  'Capacidade de expandir uma resposta curta quando convidada.']},
 2: {'objetivo': 'Contar a hist&oacute;ria da empresa em quatro marcos e dizer como ela est&aacute; organizada hoje.',
     'produto': ('Narrativa apoiada dos quatro marcos at&eacute; a organiza&ccedil;&atilde;o de hoje, com o papel dela e os '
                 'n&uacute;meros gerais &mdash; num turno s&oacute;, com uma pergunta de follow-up.'),
     'criterio': 'Os quatro marcos chegam com liga&ccedil;&atilde;o entre eles, e a &aacute;rea dela aparece sem virar lista.',
     'antes': ['Tenha a linha do tempo do deck &agrave; m&atilde;o para conferir datas &mdash; n&atilde;o para projetar.'] + _ANTES_FIXO,
     'observar': ['Quatro marcos, n&atilde;o treze datas.',
                  'Se <em>sales representative</em> sai com o sentido certo.',
                  'Se ela usa <em>this allowed us to</em> para ligar dois marcos.',
                  'Se ela assume os n&uacute;meros que s&atilde;o dela e encaminha o resto.',
                  'Continuidade entre hist&oacute;ria e &aacute;rea, sem pausa longa.',
                  'Precis&atilde;o factual: 1988, 1996, 146 employees.']},
 3: {'objetivo': 'Apresentar o portf&oacute;lio por categorias e nomear os parceiros, sem entrar em participa&ccedil;&atilde;o.',
     'produto': ('Vis&atilde;o geral do portf&oacute;lio: quatro categorias, um exemplo por categoria e as marcas &mdash; '
                 'com a recusa da participa&ccedil;&atilde;o por parceiro feita sem perder o ritmo.'),
     'criterio': 'A forma (quatro categorias) chega antes do detalhe, e a recusa n&atilde;o interrompe a apresenta&ccedil;&atilde;o.',
     'antes': ['A participa&ccedil;&atilde;o por parceiro &eacute; conte&uacute;do da aula 5 e &eacute; confidencial. Hoje ela encaminha.'] + _ANTES_FIXO,
     'observar': ['Quatro categorias antes de qualquer produto.',
                  'Um exemplo por categoria &mdash; e ela para.',
                  'Se a categoria responde quando o nome do produto n&atilde;o vem.',
                  'Se ela nomeia a Carestream corretamente.',
                  'Se a recusa sai calma e a frase continua.',
                  'Precis&atilde;o factual: as quatro categorias, as marcas do deck.']},
 4: {'objetivo': 'Responder cobertura e servi&ccedil;o como uma resposta s&oacute;, com um benef&iacute;cio operacional.',
     'produto': ('A resposta &agrave; pergunta de decis&atilde;o &mdash; quem instala e quem mant&eacute;m &mdash; com a '
                 'cobertura junto e a equipe pr&oacute;pria como benef&iacute;cio.'),
     'criterio': 'As duas metades chegam ligadas, e o que n&atilde;o est&aacute; no deck &eacute; encaminhado sem improviso.',
     'antes': ['Tempo de resposta <strong>n&atilde;o est&aacute;</strong> no deck. A resposta certa &eacute; confirmar depois.'] + _ANTES_FIXO,
     'observar': ['As duas metades chegam juntas.',
                  'Uso de <em>in-house</em>, e se ela sabe por que isso importa para ele.',
                  'Se ela recusa o tempo de resposta sem se desculpar duas vezes.',
                  'Se a cobertura sai como opera&ccedil;&atilde;o, n&atilde;o como mapa.',
                  'Continuidade quando a palavra de servi&ccedil;o n&atilde;o vem.',
                  'Precis&atilde;o factual: sede, filiais, o que a equipe inclui.']},
 5: {'objetivo': 'Dar uma mensagem por gr&aacute;fico e sustentar o Q&amp;A quando o dado n&atilde;o se confirma.',
     'produto': ('Mensagem principal por gr&aacute;fico priorit&aacute;rio, um n&uacute;mero, uma compara&ccedil;&atilde;o e '
                 'duas oportunidades &mdash; com a recusa do que n&atilde;o foi fornecido.'),
     'criterio': 'Uma frase por gr&aacute;fico, oportunidade dita como oportunidade, e nenhuma estimativa inventada.',
     'antes': ['<strong>Confirme a autoriza&ccedil;&atilde;o dos n&uacute;meros antes desta aula.</strong> Receita, lucro e '
               'mix entram; receita recorrente e comiss&otilde;es n&atilde;o. Se a autoriza&ccedil;&atilde;o n&atilde;o vier a '
               'tempo, rode com percentuais e sem valores absolutos.'] + _ANTES_FIXO,
     'observar': ['Uma frase por gr&aacute;fico &mdash; e nenhuma leitura de tabela.',
                  'Oportunidade dita como possibilidade, n&atilde;o como plano.',
                  'Se a recusa vem sem hesita&ccedil;&atilde;o longa.',
                  'Se ela volta ao fio depois da pergunta dif&iacute;cil.',
                  'Uso de <em>increased from&hellip; to&hellip;</em> e <em>accounts for</em>.',
                  'Precis&atilde;o factual: 87,7 &rarr; 105,6; 18% &rarr; 38%.']},
 6: {'objetivo': 'Rodar a reuni&atilde;o inteira, com interrup&ccedil;&otilde;es, como ser&aacute; em 31/08.',
     'produto': 'Apresenta&ccedil;&atilde;o funcional com apoio, Q&amp;A previs&iacute;vel e estrat&eacute;gias de reparo.',
     'criterio': 'Os cinco blocos chegam, ela volta ao ponto depois de cada interrup&ccedil;&atilde;o e fecha a reuni&atilde;o.',
     'antes': ['<strong>Nada de conte&uacute;do novo hoje.</strong> Se algo n&atilde;o entrou at&eacute; a aula 5, n&atilde;o '
               'entra. Comece pelo bloco que ela nomear como o mais dif&iacute;cil.'] + _ANTES_FIXO,
     'observar': ['Os cinco blocos aparecem, na ordem.',
                  'Ela volta ao ponto depois de cada interrup&ccedil;&atilde;o.',
                  'Encaminhamento em vez de improviso.',
                  'Se ela checa a pergunta antes de responder, quando n&atilde;o entendeu.',
                  'Se a vers&atilde;o curta de um bloco existe quando o tempo aperta.',
                  'Se ela fecha a reuni&atilde;o em vez de deixar no ar.']},
}
