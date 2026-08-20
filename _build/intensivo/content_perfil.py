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
    'subtitulo': ('Intensivo de seis aulas para uma reuni&atilde;o: 31 de agosto, o presidente da '
                  'Carestream na sede de S&atilde;o Paulo, com a Rita abrindo a apresenta&ccedil;&atilde;o.'),
    'info': ['Diretora de Corporate Management', 'Imagem Healthcare Solutions', 'S&atilde;o Paulo, SP'],
}

# ---------------------------------------------------------------- aba Perfil
PERFIL_PROF = """
  <p class="eyebrow">Perfil da aluna</p>
  <h2 class="sec">Perfil profissional e uso do ingl&ecirc;s</h2>
  <div class="brief">
    <dl>
      <dt>Cargo</dt><dd>Diretora de Corporate Management na Imagem Healthcare Solutions.</dd>
      <dt>Escopo</dt><dd>TI, RH, qualidade, controladoria corporativa e processos de neg&oacute;cio &mdash; equipe de nove pessoas.</dd>
      <dt>Reporta a</dt><dd>Thomaz Rodrigues (CEO). Integra o conselho.</dd>
      <dt>Uso do ingl&ecirc;s</dt><dd>Recep&ccedil;&atilde;o de visitantes internacionais e apresenta&ccedil;&atilde;o institucional da empresa. N&atilde;o &eacute; uso di&aacute;rio: &eacute; uso de alto risco, concentrado em poucos momentos.</dd>
    </dl>
  </div>

  <h3 class="sub">N&iacute;vel por habilidade</h3>
  <p class="prep-p">A2+ <strong>assim&eacute;trico</strong>: a compreens&atilde;o est&aacute; acima da produ&ccedil;&atilde;o. Ela entende
     o que o visitante pergunta bem antes de conseguir formular a resposta &mdash; e &eacute; nessa dist&acirc;ncia
     que a conversa trava. O intensivo trabalha a produ&ccedil;&atilde;o, n&atilde;o a compreens&atilde;o.</p>

  <h2 class="sec">Objetivos e prioridades</h2>
  <div class="brief">
    <dl>
      <dt>Objetivo &uacute;nico</dt><dd>Conduzir a sua parte da reuni&atilde;o de 31 de agosto, em ingl&ecirc;s, com os slides e o mapa de fala &agrave; frente.</dd>
      <dt>Prioridade 1</dt><dd>Continuidade: seguir falando quando uma palavra n&atilde;o vem.</dd>
      <dt>Prioridade 2</dt><dd>Precis&atilde;o do dado: dizer o n&uacute;mero que ela tem e encaminhar o que n&atilde;o tem.</dd>
      <dt>Prioridade 3</dt><dd>Reparo: pedir repeti&ccedil;&atilde;o e retomar o fio depois da interrup&ccedil;&atilde;o.</dd>
    </dl>
  </div>

  <h2 class="sec">Pontos de acompanhamento</h2>
  <div class="brief">
    <dl>
      <dt>Risco central</dt><dd>Colapso quando uma palavra bloqueia a sequ&ecirc;ncia. Por isso a estrat&eacute;gia de reparo entra j&aacute; na aula 1, e n&atilde;o no fim do programa.</dd>
      <dt>Apoio</dt><dd>Slide e mapa de fala ficam com ela <strong>na reuni&atilde;o</strong>. N&atilde;o s&atilde;o andaime a retirar &mdash; consultar n&atilde;o &eacute; falha.</dd>
      <dt>Sucesso</dt><dd>Efic&aacute;cia, continuidade, inteligibilidade, precis&atilde;o do dado e reparo. N&atilde;o &eacute; aus&ecirc;ncia de erro.</dd>
      <dt>Encaminhar</dt><dd>Conta como sucesso, nunca como fuga. &Eacute; o que um diretor faz numa reuni&atilde;o real.</dd>
    </dl>
  </div>

  <h2 class="sec">Pontos fortes e necessidades</h2>
  <div class="grid2">
    <div class="card"><h4>For&ccedil;as a explorar</h4>
      <ul class="prep-list">
        <li>Conhece a empresa por dentro: os n&uacute;meros, a hist&oacute;ria e os parceiros s&atilde;o dela, n&atilde;o de um script.</li>
        <li>Compreens&atilde;o auditiva acima da produ&ccedil;&atilde;o &mdash; ela entende a pergunta.</li>
        <li>Autoridade de cargo: encaminhar &eacute; leg&iacute;timo na posi&ccedil;&atilde;o dela.</li>
      </ul></div>
    <div class="card"><h4>Pontos de melhoria</h4>
      <ul class="prep-list">
        <li>Frase longa que trava no meio e recome&ccedil;a do zero.</li>
        <li>Tradu&ccedil;&atilde;o mental do portugu&ecirc;s, que atrasa a resposta e quebra o ritmo.</li>
        <li>Tend&ecirc;ncia a listar (produtos, estados, datas) em vez de dar a forma antes do detalhe.</li>
      </ul></div>
  </div>

  <h2 class="sec">Crit&eacute;rios de acompanhamento</h2>
  <h3 class="sub">Camadas de exig&ecirc;ncia por aula</h3>
  <div class="brief">
    <dl>
      <dt>Essential</dt><dd>Welcome &middot; nome e cargo &middot; o que a empresa faz &middot; o que a &aacute;rea dela cobre. Produzido sem consulta.</dd>
      <dt>With support</dt><dd>Marcos da hist&oacute;ria, categorias do portf&oacute;lio, n&uacute;meros por &aacute;rea &mdash; ela consulta o mapa.</dd>
      <dt>Recognize</dt><dd>Detalhe financeiro fora do deck, decis&atilde;o comercial, escopo de outras diretorias &mdash; ela encaminha.</dd>
    </dl>
  </div>
  <h3 class="sub">Confidencialidade</h3>
  <p class="prep-p">Receita, lucro l&iacute;quido e participa&ccedil;&atilde;o por parceiro entram <strong>a partir da aula 5</strong> e est&atilde;o
     autorizados para esta reuni&atilde;o. Confirme antes da aula 5. Comiss&otilde;es e receita recorrente <strong>n&atilde;o</strong>
     foram fornecidas: n&atilde;o s&atilde;o esquecimento dela, e a resposta correta &eacute; encaminhar.</p>
"""

PLANNING_ALUNO = """
  <p class="eyebrow">Your planning</p>
  <h2 class="sec">Six lessons, one meeting</h2>
  <p class="prep-p">On 31 August the president of Carestream comes to the head office in
     S&atilde;o Paulo and you open the presentation. These six lessons build that meeting, one block
     at a time. Your slides and your speaking map stay with you &mdash; in every lesson and in the
     meeting itself.</p>
  <div class="tbl-wrap"><table class="data" style="min-width:560px">
    <thead><tr><th style="width:74px">Lesson</th><th style="width:210px">Topic</th><th>What you will do</th></tr></thead>
    <tbody>
      <tr><td>01 &middot; 20 Aug</td><td data-lf="topico1">&mdash;</td><td>Open the meeting: who you are, what the company does, what your area covers.</td></tr>
      <tr><td>02 &middot; 24 Aug</td><td data-lf="topico2">&mdash;</td><td>Tell 38 years in four moments, and say where you sit today.</td></tr>
      <tr><td>03 &middot; 25 Aug</td><td data-lf="topico3">&mdash;</td><td>Present the portfolio in four categories, and name the partners.</td></tr>
      <tr><td>04 &middot; 26 Aug</td><td data-lf="topico4">&mdash;</td><td>Say where the company operates and who keeps the equipment running.</td></tr>
      <tr><td>05 &middot; 27 Aug</td><td data-lf="topico5">&mdash;</td><td>Give each chart one sentence, and handle the question you cannot answer.</td></tr>
      <tr><td>06 &middot; 28 Aug</td><td data-lf="topico6">&mdash;</td><td>Run the whole meeting, with interruptions.</td></tr>
    </tbody>
  </table></div>
  <h3 class="sub">How each lesson works</h3>
  <div class="brief"><dl>
    <dt>Pre-class</dt><dd>15&ndash;20 minutes on your own. No recording. The lesson works even if you do not finish it.</dd>
    <dt>In-class</dt><dd>60 minutes with your teacher. You speak; the screen is the teacher&rsquo;s.</dd>
    <dt>Post-class</dt><dd>15&ndash;20 minutes to keep what you built, and one line to bring to the next lesson.</dd>
  </dl></div>
"""

SYLLABUS = """
  <p class="eyebrow">Planejamento</p>
  <h2 class="sec">Seis aulas, uma reuni&atilde;o</h2>
  <p class="prep-p">Intensivo de <strong>seis aulas ESP</strong> entre 20 e 28 de agosto, com a reuni&atilde;o em
     31 de agosto. N&atilde;o h&aacute; rod&iacute;zio de modalidade aqui: as seis aulas t&ecirc;m o mesmo framework
     (<strong>Personalized Real-World English</strong>, oito etapas, 55 minutos de percurso essencial)
     porque o programa inteiro serve a um &uacute;nico evento comunicativo &mdash; e cada aula entrega um bloco
     dele. A aula 6 n&atilde;o traz conte&uacute;do novo: &eacute; a reuni&atilde;o inteira, uma vez.</p>

  <div class="tbl-wrap"><table class="data" style="min-width:640px">
    <thead><tr><th style="width:66px">Aula</th><th style="width:96px">Data</th><th style="width:74px">Modalidade</th><th>Tema e produto da aula</th></tr></thead>
    <tbody>
      <tr><td>01</td><td>20/08</td><td data-lf="modtag1">&mdash;</td><td><strong>Abertura da reuni&atilde;o.</strong> Quatro movimentos, cinco linhas e a primeira estrat&eacute;gia de reparo.</td></tr>
      <tr><td>02</td><td>24/08</td><td data-lf="modtag2">&mdash;</td><td><strong>Hist&oacute;ria e organiza&ccedil;&atilde;o.</strong> Quatro momentos em 38 anos e a &aacute;rea dela em uma frase.</td></tr>
      <tr><td>03</td><td>25/08</td><td data-lf="modtag3">&mdash;</td><td><strong>Portf&oacute;lio e parceiros.</strong> Quatro categorias com um exemplo cada; recusa da participa&ccedil;&atilde;o por parceiro.</td></tr>
      <tr><td>04</td><td>26/08</td><td data-lf="modtag4">&mdash;</td><td><strong>Cobertura e servi&ccedil;o.</strong> Uma resposta em duas metades, com o n&uacute;mero que ela tem.</td></tr>
      <tr><td>05</td><td>27/08</td><td data-lf="modtag5">&mdash;</td><td><strong>Resultados e crescimento.</strong> Uma frase por gr&aacute;fico e oportunidade dita como possibilidade.</td></tr>
      <tr><td>06</td><td>28/08</td><td data-lf="modtag6">&mdash;</td><td><strong>Simula&ccedil;&atilde;o completa.</strong> Cinco blocos, duas interrup&ccedil;&otilde;es, nada de conte&uacute;do novo.</td></tr>
    </tbody>
  </table></div>

  <h2 class="sec">Crit&eacute;rios de sucesso e onde s&atilde;o medidos</h2>
  <div class="tbl-wrap"><table class="data" style="min-width:560px">
    <thead><tr><th style="width:190px">Crit&eacute;rio</th><th style="width:130px">Onde &eacute; medido</th><th>O que conta como sucesso</th></tr></thead>
    <tbody>
      <tr><td>Efic&aacute;cia</td><td>Etapa 6 de cada aula</td><td>O visitante recebe a informa&ccedil;&atilde;o do bloco sem precisar perguntar de novo.</td></tr>
      <tr><td>Continuidade</td><td>Etapas 5 e 6</td><td>A frase que trava n&atilde;o derruba o bloco: ela retoma.</td></tr>
      <tr><td>Precis&atilde;o do dado</td><td>Aulas 2, 4 e 5</td><td>Diz o n&uacute;mero que tem; encaminha o que n&atilde;o tem, sem inventar.</td></tr>
      <tr><td>Reparo</td><td>Aulas 1 e 6</td><td>Pede repeti&ccedil;&atilde;o, encaminha ou adia &mdash; e volta ao ponto onde parou.</td></tr>
      <tr><td>Inteligibilidade</td><td>Todas</td><td>&Eacute; entendida na primeira vez em fala prolongada.</td></tr>
    </tbody>
  </table></div>

  <h2 class="sec">Regras que valem em toda aula</h2>
  <ul class="prep-list">
    <li>Slides e mapa de fala ficam com a aluna, inclusive na reuni&atilde;o. Consultar n&atilde;o &eacute; falha.</li>
    <li>Nenhum n&uacute;mero fora do deck. Encaminhar &eacute; a resposta certa, e conta como sucesso.</li>
    <li>A produ&ccedil;&atilde;o inicial (etapa 3) vem antes de qualquer modelo. O modelo s&oacute; existe para comparar.</li>
    <li>Um ponto de melhoria por aula &mdash; o de maior impacto. Nunca uma lista.</li>
    <li>A aula 6 n&atilde;o introduz conte&uacute;do. Se algo n&atilde;o entrou at&eacute; a 5, n&atilde;o entra.</li>
  </ul>
"""

# ------------------------------------------------- cartao da aula: preparacao
PREP = {
 1: {'objetivo': 'Abrir a reuni&atilde;o de 31 de agosto em quatro movimentos e sustentar a fala quando uma palavra n&atilde;o vier.',
     'produto': 'A abertura completa, de <em>Welcome</em> at&eacute; o que a &aacute;rea dela cobre, dita uma vez sem interrup&ccedil;&atilde;o.',
     'antes': ['Anote as palavras exatas da primeira vers&atilde;o dela (etapa 3). Elas voltam na etapa 7 e na aula 6.',
               'Confirme que ela ter&aacute; os slides na reuni&atilde;o &mdash; o material assume que sim.',
               'Nenhum material externo &eacute; necess&aacute;rio.'],
     'observar': ['Os quatro movimentos aparecem, e na ordem.', 'O que ela faz quando uma palavra n&atilde;o vem.',
                  'Se o cargo sai completo ou vira lista sem fim.', 'Se ela encaminha em vez de inventar.']},
 2: {'objetivo': 'Contar 38 anos em quatro momentos e dizer onde ela est&aacute; na empresa hoje.',
     'produto': 'Hist&oacute;ria mais &aacute;rea num turno s&oacute;, com uma pergunta de follow-up.',
     'antes': ['Tenha a linha do tempo do deck &agrave; m&atilde;o para conferir datas &mdash; n&atilde;o para projetar.',
               'A quest&atilde;o desta aula &eacute; comprimento: corte cedo, n&atilde;o no fim.',
               'Se ela citar 2025 (governan&ccedil;a), aceite como linha de apoio, fora dos quatro.'],
     'observar': ['Quatro momentos, n&atilde;o treze datas.', 'Se <em>sales representative</em> sai com o sentido certo.',
                  'Se ela assume o n&uacute;mero nove e encaminha o resto.', 'Liga&ccedil;&atilde;o entre hist&oacute;ria e &aacute;rea, sem pausa longa.']},
 3: {'objetivo': 'Apresentar o portf&oacute;lio em quatro categorias com um exemplo cada, e recusar a participa&ccedil;&atilde;o por parceiro.',
     'produto': 'O portf&oacute;lio inteiro num turno, com os parceiros nomeados e a recusa feita sem perder o ritmo.',
     'antes': ['A participa&ccedil;&atilde;o por parceiro &eacute; conte&uacute;do da aula 5 e &eacute; confidencial. Hoje ela encaminha.',
               'Pe&ccedil;a que ela comece pela categoria que interessa ao visitante, n&atilde;o pela ordem do slide.',
               'Se um produto n&atilde;o vier em ingl&ecirc;s, a categoria responde.'],
     'observar': ['Quatro categorias antes de qualquer produto.', 'Um exemplo por categoria &mdash; e ela para.',
                  'Se ela nomeia a Carestream corretamente.', 'Se a recusa sai calma e a frase continua.']},
 4: {'objetivo': 'Responder cobertura e servi&ccedil;o como uma resposta s&oacute;, com o n&uacute;mero que ela tem.',
     'produto': 'A resposta &agrave; pergunta de decis&atilde;o: quem instala e quem mant&eacute;m, com a cobertura junto.',
     'antes': ['Tempo de resposta N&Atilde;O est&aacute; no deck. A resposta certa &eacute; confirmar depois.',
               'A metade forte &eacute; o servi&ccedil;o pr&oacute;prio. Se ela come&ccedil;ar pela geografia, deixe terminar e retome no retask.',
               'Trinta t&eacute;cnicos &eacute; n&uacute;mero do deck: ela pode dizer.'],
     'observar': ['As duas metades chegam juntas.', 'Uso de <em>our own service team</em>.',
                  'Se ela recusa o SLA sem se desculpar duas vezes.', 'Se a cobertura sai como opera&ccedil;&atilde;o, n&atilde;o como mapa.']},
 5: {'objetivo': 'Resumir cada gr&aacute;fico em uma frase e recusar o n&uacute;mero que nunca lhe foi dado.',
     'produto': 'Os tr&ecirc;s resumos mais duas oportunidades, com duas perguntas de press&atilde;o em cima.',
     'antes': ['CONFIRME a autoriza&ccedil;&atilde;o dos n&uacute;meros antes desta aula. Receita, lucro e mix entram; receita recorrente e comiss&otilde;es n&atilde;o.',
               'Se a autoriza&ccedil;&atilde;o n&atilde;o vier a tempo, rode a aula com os percentuais e sem os valores absolutos.',
               'Ela sabe os n&uacute;meros. O trabalho aqui &eacute; n&atilde;o l&ecirc;-los.'],
     'observar': ['Uma frase por gr&aacute;fico &mdash; e nenhuma leitura de tabela.', 'Oportunidade dita como possibilidade.',
                  'Se a recusa vem sem hesita&ccedil;&atilde;o longa.', 'Se ela volta ao fio depois da pergunta dif&iacute;cil.']},
 6: {'objetivo': 'Rodar a reuni&atilde;o inteira, com interrup&ccedil;&otilde;es, exatamente como ser&aacute; em 31 de agosto.',
     'produto': 'Os cinco blocos, duas interrup&ccedil;&otilde;es e o fechamento feito por ela.',
     'antes': ['Nada de conte&uacute;do novo hoje. Se algo n&atilde;o entrou at&eacute; a aula 5, n&atilde;o entra.',
               'Comece pelo bloco que ela nomear como o mais dif&iacute;cil.',
               'Interrompa duas vezes, e uma delas com pergunta que n&atilde;o &eacute; da &aacute;rea dela.'],
     'observar': ['Os cinco blocos aparecem, na ordem.', 'Ela volta ao ponto depois de cada interrup&ccedil;&atilde;o.',
                  'Encaminhamento em vez de improviso.', 'Se ela fecha a reuni&atilde;o em vez de deixar no ar.']},
}
