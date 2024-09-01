from BancoDeDados import Session
from calendar import month_name
from sqlalchemy.sql import func
import pandas as pd
from tabelas import Product, ProductCategory, ProductSubcategory, Sales, Customer, Territory, Return
import matplotlib.pyplot as plt

session = Session()

# Consulta para encontrar o faturamento total mensal para o ano de 2016
result = session.query(
    func.extract('month', Sales.orderdate).label('month'),  # Extrai o mês da data do pedido e o rotula como 'month'
    func.sum(Sales.orderquantity * Product.productprice).label('total_revenue')  # Calcula o faturamento total (quantidade * preço do produto) e o rotula como 'total_revenue'
).join(
    Product  # Faz uma junção com a tabela Product
).filter(
    Sales.productkey == Product.productkey,  # Garante que o produto corresponde ao chave do produto na tabela Sales
    (Sales.orderdate >= '2016-01-01') &  # Filtra para pedidos a partir de 1º de janeiro de 2016
    (Sales.orderdate < '2017-01-01')  # Até 31 de dezembro de 2016
).group_by(
    func.extract('month', Sales.orderdate)  # Agrupa os resultados por mês
).order_by(
    func.extract('month', Sales.orderdate)  # Ordena os resultados por mês
).all()  # Executa a consulta e obtém todos os resultados

# Criar um DataFrame a partir do resultado
df = pd.DataFrame(result, columns=['Month', 'Total_Revenue'])
df.to_csv('.\Desafio 1\ResultadosCSV\FaturamentoMensal2017.csv', index=False)

# Criar o gráfico
plt.figure(figsize=(10, 6))  # Define o tamanho da figura do gráfico
plt.plot(df['Month'], df['Total_Revenue'], marker='o', linestyle='-', color='b')  # Plota o gráfico com marcadores, linha e cor azul
plt.title('Faturamento Total Mensal para o Ano de 2016')  # Define o título do gráfico
plt.xlabel('Mês')  # Rótulo do eixo X
plt.ylabel('Faturamento Total')  # Rótulo do eixo Y
plt.xticks(df['Month'], ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])  # Define os rótulos do eixo X para os meses do ano
plt.grid(True)  # Adiciona uma grade ao gráfico
plt.tight_layout()  # Ajusta o layout para não cortar elementos

# Salvar Gráficos em .png
plt.savefig('.\Gráficos\FaturamentoMensal2017.png')

# Mostrar o gráfico
plt.show()  

