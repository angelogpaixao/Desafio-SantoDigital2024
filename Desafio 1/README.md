<h1 align="center">Desafio 01</h1>

## Descrição
Este desafio foi resolvido utilizando o dataset público AdventureWorks, a fim de responder a 5 perguntas de negócio relacionadas a vendas e desempenho. O dataset utilizado foi o AdventureWorks, que contém informações detalhadas sobre vendas, produtos, clientes e vendedores. A análise foi conduzida com base nos dados relevantes para cada pergunta de negócio.

Perguntas de Negócio
* Quais são os 10 produtos mais vendidos (em quantidade) na categoria "Bicicletas", considerando apenas vendas feitas nos últimos dois anos?
* Qual é o cliente que tem o maior número de pedidos realizados, considerando apenas clientes que fizeram pelo menos um pedido em cada trimestre do último ano fiscal?
* Em qual mês do ano ocorrem mais vendas (em valor total), considerando apenas os meses em que a receita média por venda foi superior a 500 unidades monetárias?
* Quais vendedores tiveram vendas com valor acima da média no último ano fiscal e também tiveram um crescimento de vendas superior a 10% em relação ao ano anterior?
* Extra: Qual o faturamento total mensal para o ano de 2016?

Além disso, foram criados três gráficos de visualização para:
* Os 10 produtos mais vendidos na categoria de "Bicicletas".
* Um mapa de calor que ilustra as vendas por região e por mês.
* Um gráfico que mostra a evolução do faturamento mensal de 2016.

## Ferramentas Utilizadas

* Python
* VScode
* SQLAlchemy
* Pandas
* Mathplotlib
* Seaborn
* Calendar

## Como utilizar o código

O banco de dados utilizado é o SQLite, portanto, basta executar o arquivo criartabelas.py para que as tabelas necessárias sejam criadas. Em seguida, utilize o arquivo importacaocsv.py para importar os dados. Esse script processará automaticamente todos os arquivos CSV presentes no repositório. Para finalizar, execute os scripts de query que têm o sufixo QN, correspondendo a cada questão, como Q1_Top10BikesMaisVendidas, Q2_ClienteComMaisPedidos, etc. Esses scripts irão gerar os arquivos CSV com os dados solicitados e, conforme a questão, também produzir gráficos de visualização.
