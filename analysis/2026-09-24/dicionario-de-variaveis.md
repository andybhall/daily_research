# Dicionário de variáveis

Conjunto: *Deepfakes, direitos humanos e regulação: levantamento documental e jurisprudencial (2018–2026)*, versão 2.0
Arquivo descrito: `deepfakes_levantamento_v2.csv` — 129 registros, 11 campos, codificação UTF-8, delimitador vírgula, aspas duplas como qualificador de texto, primeira linha com nomes de campo.

Cada linha corresponde a um documento (acórdão, ato normativo, informe institucional ou relatório de pesquisa). A estrutura é plana: não há chave estrangeira nem tabela relacionada.

O esquema reproduz o do painel `dashboard_deepfakes.html`, com nomes de campo em português e sem abreviação. A correspondência entre os dois é a seguinte:

| Campo no CSV | Campo no painel | Origem |
|---|---|---|
| `id` | — | gerado na normalização |
| `jurisdicao` | `jurisdicao` | nome da aba |
| `secao` | `secao` | linha de cabeçalho na planilha |
| `referencia_completa` | `titulo` | coluna A |
| `autor_orgao` | `autor` | coluna B |
| `tipo_documento` | `tipo` | coluna C |
| `tipo_grupo` | `tipoGrupo` | derivado de `tipo_documento` |
| `temas_centrais` | `temas` | coluna D |
| `resumo_analitico` | `resumo` | coluna E |
| `localizacao` | `localizacao` | coluna G |
| `url` | `url` | derivado de `localizacao` |

O painel mantém ainda dois campos sem correspondente no CSV. `temasList` é o desdobramento de `temas_centrais` em vetor, obtido por separação no ponto e vírgula e supressão do ponto final; não foi replicado como coluna por ser reconstruível de forma trivial (v. regra em `temas_centrais`). `categorias` corresponde à coluna F da planilha, hoje integralmente vazia e por isso suprimida.

---

## Visão geral dos campos

| Campo | Tipo | Preenchimento | Vocabulário |
|---|---|---:|---|
| `id` | texto | 129/129 | controlado (gerado) |
| `jurisdicao` | categórico | 129/129 | controlado, 3 valores |
| `secao` | categórico | 129/129 | controlado, 12 valores |
| `referencia_completa` | texto livre | 129/129 | padrão ABNT |
| `autor_orgao` | categórico | 129/129 | semicontrolado |
| `tipo_documento` | categórico | 129/129 | semicontrolado, 22 valores |
| `tipo_grupo` | categórico | 129/129 | controlado, 4 valores |
| `temas_centrais` | texto livre | 129/129 | não controlado |
| `resumo_analitico` | texto livre | 129/129 | — |
| `localizacao` | texto livre | 128/129 | — |
| `url` | URL | 127/129 | — |

---

## Descrição campo a campo

### `id`
Identificador único, atribuído na normalização e sem correspondente na planilha ou no painel. Formato `XX-NNN`, em que o prefixo indica a aba de origem (`BR`, `SI`, `ON`) e o sufixo é sequencial de três dígitos na ordem de leitura. Serve para referência estável entre a base, este dicionário e eventuais análises; não possui significado jurídico e não deve ser citado como identificador do documento, papel que cabe à `referencia_completa`.

Atenção: a numeração é **relativa à versão**. Registros suprimidos ou incorporados deslocam os sufixos, de modo que `BR-045` na versão 2.0 não corresponde necessariamente ao mesmo documento em versão futura. Referências cruzadas entre versões devem apoiar-se na referência completa.

### `jurisdicao`
Ordenamento jurídico ou sistema normativo ao qual o documento pertence. Vocabulário controlado, três valores: `Brasil` (73), `ONU / UNICEF / União Europeia` (48), `Sistema Interamericano (SIDH)` (8). Na planilha a informação está implícita no nome da aba; foi promovida a coluna na normalização.

O painel declara internamente quatro jurisdições, incluindo `Estados Unidos (EUA)`, hoje sem registros correspondentes na planilha. A discrepância está documentada na advertência preliminar do README e deve ser resolvida antes do depósito.

Observe-se que o valor `ONU / UNICEF / União Europeia` agrega três ordens distintas — sistema onusiano, União Europeia e legislação nacional europeia (Código Penal francês, Online Safety Act britânico). A agregação foi herdada da planilha e preservada por fidelidade; análises que dependam da distinção entre direito internacional e direito interno europeu devem desagregar o campo com apoio em `secao` e `autor_orgao`.

### `secao`
Agrupamento temático interno da jurisdição, derivado dos cabeçalhos que na planilha ocupam linhas próprias. Doze valores: `TRIBUNAL SUPERIOR ELEITORAL - TSE`, `TRIBUNAIS REGIONAIS ELEITORAIS - TREs`, `RESOLUÇÕES E PORTARIAS DO TSE`, `AGÊNCIA NACIONAL DE PROTEÇÃO DE DADOS - ANPD`, `OUTROS ÓRGÃOS TÉCNICOS (MJSP, AGU, CGI.BR, CNMP, etc.)`, `SOCIEDADE CIVIL (OUTROS DOCUMENTOS)`, `LEGISLAÇÃO BRASILEIRA`, `INFORMES ANUAIS, SOBRE PAÍSES E TEMÁTICOS`, `OUTROS DOCUMENTOS DO SIDH`, `INFORMES, DOCUMENTOS E COMUNICADOS DE IMPRENSA`, `OUTROS DOCUMENTOS ONU (ECHR, COUNCIL OF EUROPE, EDPS)`, `LEGISLAÇÃO EUROPEIA`.

O campo mistura dois critérios classificatórios — natureza do documento e órgão emissor —, o que impede seu uso isolado como variável de classificação. Para segmentar por natureza documental, use `tipo_grupo`.

### `referencia_completa`
Referência bibliográfica em padrão ABNT, redigida manualmente. Para precedentes judiciais, contém o tribunal, a classe e o número do processo, o relator, a data do acórdão e os dados de publicação no diário eletrônico. É o identificador canônico do documento e o elemento pelo qual cada decisão deve ser recuperada nas bases de jurisprudência, dada a instabilidade das URLs (v. `url`).

Não há campo de data isolado. Séries temporais exigem extração da data a partir desta cadeia de texto, cujo padrão predominante nos acórdãos é `Acórdão de DD/MM/AAAA`; a expressão regular `Acórdão de (\d{2}/\d{2}/\d{4})` recupera as 47 datas de julgamento. A extração é viável, mas exige verificação: muitos registros trazem duas datas (julgamento e publicação) e os documentos não judiciais seguem padrões variados, por vezes apenas com ano.

### `autor_orgao`
Órgão emissor, autoridade ou, no caso de atos normativos, denominação abreviada da norma. Vocabulário semicontrolado. Predominam siglas de tribunais no padrão `TRE-XX`, presentes para 19 unidades federativas, além de `TSE`.

Registre-se uma inconsistência de categoria herdada da planilha: em parte dos registros de legislação, o campo foi preenchido com o nome da norma (`LGPD`, `MARCO CIVIL DA INTERNET`, `AI ACT`, `DIGITAL SERVICES ACT`, `ECA DIGITAL`, `DECRETO N° 12.976/2026`) em vez do órgão emissor. A opção é compreensível na lógica de fichamento, mas contamina contagens por autoria. Recomenda-se, em versão futura, desdobrar o campo em `orgao_emissor` e `denominacao_norma`.

Há ainda um registro em que a autoria institucional foi atribuída a `UNICEF` quando o documento é assinado por ONU Mulheres e pela Sexual Violence Research Initiative.

### `tipo_documento`
Natureza formal do documento, conforme registrada pelos pesquisadores. Vinte e dois valores: `PRECEDENTE JUDICIAL` (47), `INFORME - RELATORIA ESPECIAL DA ONU` (13), `DOCUMENTO` (12), `RESOLUÇÃO` (12), `DOCUMENTO DE PESQUISA` (8), `RELE` (5), `LEGISLAÇÃO` (5), `LEI` (4), `COMUNICADO DE IMPRENSA` (4), `RESOLUÇÃO TSE` (3), `NOTA TÉCNICA` (3), `RELATÓRIO DE PESQUISA` (3), e com ocorrência única `PORTARIA TSE`, `DECRETO`, `RECOMENDAÇÃO`, `RECOMENDAÇÃO CONJUNTA`, `RECOMENDAÇÃO GERAL`, `INFORME/DOCUMENTO`, `RELATÓRIO`, `RELATÓRIO ANUAL`, `GUIDELINES`, `DECLARAÇÃO CONJUNTA`.

O vocabulário não é ortogonal (v. seção 6 do README). Use `tipo_grupo` para agregação.

### `tipo_grupo`
**Campo derivado**, ausente da planilha e criado para replicar no CSV a classificação em quatro naturezas que o painel utiliza nos indicadores e no gráfico de rosca. Valores e frequências: `Documento institucional / Informe` (56), `Precedente judicial` (47), `Resolução / Portaria` (16), `Legislação` (10).

Regra de derivação, a partir de `tipo_documento`:

| `tipo_grupo` | Valores de origem |
|---|---|
| Precedente judicial | `PRECEDENTE JUDICIAL` |
| Legislação | `LEI`, `DECRETO`, `LEGISLAÇÃO` |
| Resolução / Portaria | `RESOLUÇÃO`, `RESOLUÇÃO TSE`, `PORTARIA TSE` |
| Documento institucional / Informe | todos os demais |

Duas ressalvas. A primeira é que dois valores presentes nesta versão — `RECOMENDAÇÃO` (CNMP nº 125/2026) e `RECOMENDAÇÃO GERAL` (Comitê CEDAW) — não existiam quando o painel foi gerado e, portanto, não constam de sua tabela de correspondência original. Foram classificados como documento institucional por analogia a `RECOMENDAÇÃO CONJUNTA`, que o painel já tratava assim. A classificação é discutível: a Recomendação do CNMP tem eficácia normativa interna sobre os ramos do Ministério Público, e um critério centrado em força vinculante a alocaria em `Resolução / Portaria`. Se a distinção importar para a análise, reclassifique explicitamente e regere o painel.

A segunda é que a fronteira entre `Legislação` e `Resolução / Portaria` separa fonte legislativa em sentido estrito de ato infralegal de autoridade administrativa ou judiciária — distinção pertinente no ordenamento brasileiro, em que as resoluções do TSE ocupam posição peculiar, mas que se torna artificial quando aplicada a resoluções da Assembleia Geral da ONU, cuja natureza é diversa e cuja alocação neste grupo decorre apenas da coincidência de nome.

### `temas_centrais`
Palavras-chave atribuídas pelos pesquisadores, separadas por ponto e vírgula, em geral cinco por registro, com ponto final ao término da cadeia. Preenchido em todos os 129 registros.

**Regra de desdobramento** (a mesma empregada pelo painel para construir `temasList`): separar por `;`, remover espaços nas extremidades e suprimir o ponto final do último elemento. O resultado são 290 rótulos distintos, dos quais 208 ocorrem uma única vez e 39 alcançam frequência igual ou superior a três. Os mais frequentes são `Deepfakes` (112), `Liberdade de Expressão` (28), `Inteligência Artificial` (15), `Propaganda Eleitoral` (15), `Desinformação Eleitoral` (13), `WhatsApp` (11) e `Perspectiva de Gênero` (11).

Antes de qualquer contagem, três correções são necessárias. Há variação de caixa entre registros, em dez pares identificados (`Liberdade de Expressão` / `Liberdade de expressão`; `Censura Prévia` / `Censura prévia`; `Dever de Cuidado` / `Dever de cuidado`; `Plataformas Digitais` / `Plataformas digitais`; `Moderação de Conteúdo` / `Moderação de conteúdo`; `Vigilância Digital` / `Vigilância digital`; `Violência Digital de Gênero` / `Violência digital de gênero`; `Deepfakes Eleitorais` / `Deepfakes eleitorais`; `Deepfakes Sexuais` / `Deepfakes sexuais`; `Sátira Política` / `Satira Política`). Há erros tipográficos (`Sática Política`, `Direios Humanos`, `Identidades sinteticas`). E há alternância entre singular e plural (`Deepfake` / `Deepfakes`), que fragmenta artificialmente o rótulo mais frequente do conjunto.

Um registro incorpora ao final da lista de temas uma observação processual — `Tutela Cautelar. Obs: processo em segredo de justiça, íntegra não disponível, somente Ementa` —, informação relevante mas que pertence a campo de nota, não a campo de indexação, e que o desdobramento converte em pseudo-palavra-chave.

### `resumo_analitico`
Síntese descritiva e analítica do documento, redigida pelos pesquisadores. Preenchido em todos os 129 registros. Nos precedentes judiciais segue estrutura relativamente estável: identificação do órgão julgador e do caso, descrição do conteúdo impugnado, fundamentação adotada, dispositivos aplicados e formulação da *ratio decidendi* extraída pelos pesquisadores. Extensão variável, de uma frase a cerca de quatrocentas palavras.

Alguns resumos incorporam citação direta do documento-fonte entre aspas, prática mais frequente nos registros de sociedade civil e de organismos internacionais. Quem reutilizar o campo deve observar que essas passagens são reprodução de terceiros, não texto autoral dos pesquisadores, e permanecem sujeitas ao regime de direitos da fonte original.

### `localizacao`
Texto de localização no padrão ABNT, na forma `Disponível em: <URL>.`. Preenchido em 128 dos 129 registros; a ausência é o registro `BR-066` (Instituto Marielle Franco).

Para os precedentes judiciais brasileiros, o endereço aponta para o portal de consulta de jurisprudência do TSE, e não para o documento individual, em razão da instabilidade das URLs profundas da Consulta Unificada do PJe. A recuperação exige busca pelo número do processo, disponível em `referencia_completa`.

### `url`
**Campo derivado**: endereço extraído de `localizacao` pela expressão `(https?://[^\s>]+)`, com supressão de ponto final e sinal de maior nas extremidades, para permitir verificação programática de disponibilidade. Preenchido em 127 dos 129 registros.

As duas ausências são `BR-066`, por campo de origem vazio, e `SI-002`, cujo endereço foi registrado como `://www.oas.org/...`, sem o protocolo — a expressão de extração não o captura, e o documento é recuperável mediante correção do prefixo. Nenhuma verificação sistemática de disponibilidade das ligações foi realizada na data de fechamento.

---

## Campos ausentes e recomendados para versão futura

A estrutura atual não permite quatro operações analiticamente úteis, todas viabilizáveis por codificação sobre material já reunido.

Não há campo de **data em formato normalizado** (`AAAA-MM-DD`), o que impede série temporal sem processamento do texto da referência. Não há campo de **resultado do julgamento** — se o tribunal reconheceu ou afastou a configuração de *deepfake*, e se aplicou ou não sanção —, variável que, dado o objeto do artigo, é provavelmente a mais valiosa a acrescentar: permitiria quantificar a divergência entre TREs quanto ao critério de gravidade e ao ônus probatório, hoje perceptível apenas pela leitura sucessiva dos resumos. Não há campo de **fundamento normativo invocado** (art. 9º-B, art. 9º-C da Res. TSE nº 23.610/2019, art. 57-D da Lei nº 9.504/1997), recuperável apenas por leitura. E não há **codificação da plataforma** em que circulou o conteúdo impugnado — WhatsApp, Instagram, Facebook, TikTok, YouTube —, informação presente de forma consistente nos resumos e nas palavras-chave, mas não estruturada.

Acrescente-se um campo de **data de último acesso** por registro, exigência corrente do padrão ABNT para documentos eletrônicos e presentemente ausente do conjunto.
