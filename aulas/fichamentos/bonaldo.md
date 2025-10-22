# Fichamento - As palavras e os tokens

- Modelo woke apresentado:

“Esses modelos valem pelo componente fundacional de uma família de ferramentas de Processamento de Linguagem Natural (PLN). Eles são baseados em algoritmos de “aprendizado de máquina” como o Word2Vec (Mikolov et al., 2013), uma expressão – talvez por demais antropomórfica – para processamento de informação por reconhecimento de padrões com RNAs” (Bonaldo, 2024, p. 10)

- Base de dados para treinamento da RNA:

“Essas redes neurais, que possuem uma camada oculta entre a entrada e a saída, são treinadas em um banco de dados escalável, cujo primeiro lote foi exposto a 411 trabalhos defendidos no PPG em História da UFSC entre 2010 e 2023. Para o treinamento do segundo lote, coletamos a integralidade dos textos de 30.643 trabalhos, somando 96,25% dos dados nativos digitais do repositório institucional da UFSC para o período 2003-2024 – e 69,32% de todas as teses e dissertações já defendidas em nossa instituição.” (Bonaldo, 2024, p. 10)

3 modelos são apresentados no artigo:

“Woke-HST, Woke-CFH e Woke-UFSC, treinados, respectivamente, em teses e dissertações defendidas no PPG em História, nos PPGs do nosso Centro de Filosofia e Ciências Humanas, e em todas as coleções de nossa universidade.” (Bonaldo, 2024, p. 10)

Transforma tokens em vetores estruturados.

Grupo de Estudos em IA e História (UFSC):

“missão é mitigar a dependência acadêmica nos dados de treinamento e nos parâmetros de análise elaborados pelas big techs2.” (Bonaldo, 2024, p. 10)

- Passar da coleção para interpretação historiográfica
- “hermenêutica digital”
- open source

Porém:

“não devemos nos entusiasmar demais. A contribuição dos métodos que estamos desenvolvendo limita-se a traduzir princípios ético-epistemológicos da historiografia em linguagem de programação. Afinal, esse é o lugar de onde falo e a partir do qual acredito que possamos ser úteis como nunca (Lucchesi; Silveira; Nicodemo 2020).” (Bonaldo, 2024, p. 11)

### História dos conceitos + Semântica vetorial

“o significado de uma palavra-alvo é determinado pela posição ocupada por classes e subclasses gramaticais que a cercam – e estatisticamente extrapolado com base em um grande volume de dados.” (Bonaldo, 2024, p. 11)

“A estrutura distribucional da linguagem, da qual a semântica é descrita como uma função da sintaxe” (Bonaldo, 2024, p. 11)

“empregamos técnicas semasiológicas e onomasiológicas expondo os modelos a um grande conjunto de dados que permitem gerar campos semânticos vazados em gráficos” (Bonaldo, 2024, p. 11)

Representar mudanças e permanências de significados diacronicamente.

## As palavras e os tokens

Através de Word embedding Models (WEMs):

“Esse tipo de modelo permite manipular os blocos fundamentais da linguagem e as unidades simbólicas da computação: as palavras e os tokens.” (Bonaldo, 2024, p. 11)

WEM: é um modelo subsimbólico fundamentado em “representações distribuídas”: “o significado de uma palavra não é por nós programado (*harcoded*), mas identificado pela ativiação de redes neurais em uma camada mais baixa de processamento.” (Bonaldo, 2024, page 11-12)

“Essa é a verdadeira revolução atômica da IA: a quebra dos átomos indivisíveis da computação.” (Bonaldo, 2024, p. 12)

#### Embeddings

Palavras com significados similares aparecem mais próximas umas das outras. Ver exemplo de Biden e Lula e o gráfico da página 12.

[image]  
(Bonaldo, 2024, p. 12)

WEMs: permite medir taxas de variação semântica e “gerar visualizações de significados historicamente saturados, não linearmente dispostos, mas estratificados ao longo de durações”: ‘estratos do tempo’ de Koselleck.

Argumento: essa análise, se fundamentada em “vetores mais profundos e densos”, possibilitam passar de palavras a números (vetores, tokens) em pequenas passadas e não através de ‘saltos bruscos’ (12)

## Conceito: “melhor dectectável por representações distribuídas” (p.13)

“Adicionalmente, defendo a hipótese de que o caráter polissêmico, disputado, ambíguo e impreciso dos conceitos seja melhor detectável por representações distribuídas. Dito de outra forma, sustento que conceitos, por serem mais do que palavras, não possuem uma natureza simbólica, mas subsimbólica – e que suas qualidades iterativas podem ser quantificadas ao longo do tempo por taxas de variação semântica. Com isso, busco contribuir para a identificação e a análise dos conceitos “que cada vez mais passam a ocupar um papel fundamental nos debates políticos e nas formas de orientação histórica” (Turin 2023, 715)” (Bonaldo, 2024, p. 13)

Busca se afastar do neopositivismo.

“Modelos são dispositivos epistemológicos que se situam entre o documento e a explicação.” (Bonaldo, 2024, p. 14)

Heurística digital:

“Do ponto de vista da heurística das fontes, torna-se então necessário moderar o “distanciamento entre historiadores/as e a elaboração das ferramentas de pesquisa e os conjuntos de dados disponibilizados atualmente” (Brasil 2022, 213). Por isso, ao invés de propor que a matematização da história implique na transformação de nossa disciplina em “ciência positiva”, ofereço dados que introduzem – sob o signo da caixa-preta e do caráter indefinido a respeito das possibilidades da computação – elementos de incerteza e indeterminação que precisam ser reconhecidos e problematizados.” (Bonaldo, 2024, p. 14)

Ou seja, agenda teórica ligada às humanidades digitais:

“a legitimidade do objetivismo histórico – dependente não apenas da questão norteadora de uma pesquisa, mas igualmente dos problemas levantados em seu percurso” (Bonaldo, 2024, p. 14)

### Os modelos (p. 15)

Transparência:

[image]  
(Bonaldo, 2024, p. 15)

Limites:

“WEMs são capazes de representar campos semânticos de palavras alvo, mas as dimensões referenciais e contextuais (sociais) são mais desafiadores de serem capturadas por eles.” (Bonaldo, 2024, p. 16)

Exemplo: Google Ngram Viewer

“Esse é o caso do uso de N-Gramas, como o Google Ngram Viewer, em estudos de história conceitual: eles não representam conceitos, mas apenas palavras, o que potencializa o risco do essencialismo semântico.” (Bonaldo, 2024, p. 16)

#### Hermenêutica digital (p. 16)

“ousar abrir simultaneamente duas caixas-pretas. Investigar a “relação entre o que é próprio da história e o que é próprio da computação” é outra forma de enunciar esse problema (Silveira 2022, 222).” (Bonaldo, 2024, p. 17)

### Coleta dos dados (17)

Duplo gesto: heurístico e epistemológico:

“1) escolha do dataset, 2) raspagem de dados (web scraping) e 3) validação, limpeza e estruturação da coleta.” (Bonaldo, 2024, p. 17)

Explica o processo de coleta e pré-processamento dos dados (17-19)

## Ciência de dados + PLN (20)

- tokenização:

“uma cadeia de caracteres a qual é atribuída um significado ou um valor específico.” (Bonaldo, 2024, p. 20)

Spacy + NLTK

remoção de caracteres, limpeza geral, remoção de *stopwords*

- Lematização dos verbos

“PTBR-VL Toolkit,” (Bonaldo, 2024, p. 20)

- NER

“reconhecimento de entidades nomeadas” (Bonaldo, 2024, p. 20)

[O autor utliza **operação historiográfica artificial** ao longo do texto. O que quer dizer com isso?]

### treinamento de  máquina (21)

pq usar?

1. acessar, ler e interpretar quantidades massivas de dados (sempre difícil)
2. WEMs representam tokens como vetores: visualização do caráter disputado e polissêmico dos conceitos
3. “capturar significados *êmicos* minimizando o risco de imputar noções *éticas* no ponto de partica da interpretação” (21)

“Mas a IA é desprovida de intencionalidade. Isso significa que ela sequer pode incutir noções éticas por si só e que qualquer viés nos resultados do aprendizado de máquina portanto não decorre da tecnologia em si, mas da natureza dos dados e das escolhas de modelagem feitas pelos humanos que a configuram” (Bonaldo, 2024, p. 21)

#### Parâmetros = decisões teóricas?

“a estrutura e os parâmetros da análise são configurados antecipadamente. Por isso, a escolha do modelo adequado é também uma tarefa de Ciência de Dados: a qualidade dos sinais de entrada deve determinar os parâmetros escolhidos em função das questões propostas pela pesquisa.” (Bonaldo, 2024, p. 21)

[image]  
(Bonaldo, 2024, p. 22)

#### Escala dos dados (22)

1. micro-diacrônico: modelos para cada período
2. incrementais: atualiza a rede gradualmente
3. temporais: séries de modelos; novo modelo treinado tanto com os novos dados quanto com os dados da séries temporais anteriores

#### Como calcular a “variação semântica de conceitos ao longo do tempo”? (23-24)

- Similaridade de cosseno: magnitude + direção das mudanças vetoriais
- índice de Jaccard: quantificar a similaridade e a diversidade entre conjuntos de palavras + quantificar a mudança nos vizinhos semânticos ao longo do tempo

“Em nossa operação historiográfica artificial, os parâmetros – pesos em matrizes – devem fazer as vezes das hierarquias entre as durações de Braudel, ou, no contexto do diálogo do PLN com a história conceitual, entre os padrões de estabilidade e inovação na semântica dos tempos históricos de Koselleck.” (Bonaldo, 2024, p. 25)

“Nossa aposta é de que treinamentos temporais e incrementais permitirão simular melhor as características fluidas da experiência do tempo expressas pela linguagem, visando contribuir para a captura da natureza estratificada e não simultânea de sua semântica ao fazer uso de vetores densos entrelaçados em clusters historicamente saturados.” (Bonaldo, 2024, p. 25)

### Validação e ajuste fino (25)

aprendizado supervisionado: teste com uma variável alvo estabeelcida => “fazemos perguntas para as quais conhecemos as respostas corretas e atribuímos uma pontuação a cada modelo.” (Bonaldo, 2024, p. 25)”

### Visualização e análise de dados (27)

“Em nosso caso, passamos da manipulação estatística, do cálculo e da álgebra linear para métricas de similaridade, como a similaridade de cossenos, que calcula distribuições de palavras representadas como vetores normalizados no espaço de embedding.” (Bonaldo, 2024, p. 27)

Classe, raça e gênero: “qual desses conceitos é mais estável e qual é mais instável de acordo com nossos modelos? Nossa expectativa é de que “classe”, por ser o conceito mais antigo e estabelecido, seja também o mais estável.” (Bonaldo, 2024, p. 27)

- Classe distante de raça e gênero?

“Esses dados nos dizem que a frequência da coocorrência distribucional dessas palavras é rara e muito dispersa, sugerindo que trabalhos problematizando classes sociais tem outros indicadores e interesses de análise.” (Bonaldo, 2024, p. 31)

“O mesmo fenômeno não é visível entre os dois outros termos da tríade multiculturalista: “raça” é o segundo vetor mais próximo de “gênero” (0.4433887302875519) e “gênero” (0.4433887302875519) é o terceiro vetor associado à “raça”. Ou seja, a frequência da coocorrência dessas palavras em contextos linguísticos específicos é muito representativa, indicando que estudos étnico-raciais e estudos de gênero conversam muito mais entre si do que com trabalhos interessados em analisar a dinâmica de classes.” (Bonaldo, 2024, p. 31)

[image]  
(Bonaldo, 2024, p. 32)

“O conceito de classe é o membro mais estável da tríade analisada” (Bonaldo, 2024, p. 38)

“classe é também o conceito cujo campo semântico menos se intersecta com raça e gênero ao longo de toda a série.” (Bonaldo, 2024, p. 38)

“Esse pequeno experimento demonstra como é complexa a tarefa de identificar padrões de mudança semântica. Ainda assim, trata-se de um passo incontornável para que possamos encontrar os parâmetros das durações conceituais, rumo à codificação de visualizações mais complexas, capazes de representar significados não simultâneos.” (Bonaldo, 2024, p. 41)

“em vez de objetos técnicos neutros e passivos – como a palavra “ferramenta” pode vir a sugerir o aprendizado de máquina constrói modelos que se situam entre o documento e a explicação. Consequentemente, é apenas possuindo o controle dos vetores da informação que podemos realizar a engenharia reversa da caixa-preta, minerar contingências, ou executar a “função referencial” (Ifversen 2011, 77).” (Bonaldo, 2024, p. 44)

## Conclusões

“É na categoria experiência que atualmente reside a principal limitação de nossos modelos.” (Bonaldo, 2024, p. 46)

“Koselleck 3: “uma palavra se torna um conceito se a totalidade das circunstâncias político-sociais e empíricas, nas quais e para as quais essa palavra é usada, se agrega a ela” (Koselleck 2006, 109).” (Bonaldo, 2024, p. 46)

“Os métodos computacionais nos permitem observar como novos conceitos se revelam por meio de agitação e inovação linguísticas. Mas essa é apenas a sua dimensão interna. Outras se referem a elementos que estão fora da linguagem: é o “aspecto contextual do significado” (Ifversen 2011, 81), que responde pelo diálogo com a história social.” (Bonaldo, 2024, p. 46)

“A captura de espaços de experiência – compreendidos enquanto conjunto completo das situações políticas, sociais e práticas – só poderá ser automatizada com o desenvolvimento de modelos mais complexos, treinados em um banco de dados bem mais extenso e capazes de operar com milhões de parâmetros.” (Bonaldo, 2024, p. 46)

Solução: *transformers*?

“Estou convencido de que o volume massivo de documentação exigido por esse empreendimento ganhará com o emprego de métodos digitais. Entretanto, não estou convencido de que esta seja a tarefa de uma história conceitual meramente quantitativa, mas parte de um esforço coletivo por uma história digital que seja capaz de renegociar as fronteiras entre abordagens quantitativas e qualitativas (Cardoso Júnior 2023). A partir de agora, esse projeto transgeracional passa a depender de uma aliança entre duas formas de ver e interpretar o mundo: a erudição e a análise de big data.” (Bonaldo, 2024, p. 47)

### Importância de desenvolvermos nosso próprio sistema (44)