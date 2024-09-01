from BancoDeDados import Session
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from tabelas import Product, ProductCategory, ProductSubcategory, Sales, Customer, Territory, Return

session = Session()

# Consulta  para obter dados por mês e região
query = session.query(
    Territory.region,
    func.extract('month', Sales.orderdate).label('Month'), 
    func.sum(Sales.orderquantity).label('total_vendas')
).join(Sales).filter(
    (Sales.orderdate >= '2015-01-01') &
    (Sales.orderdate < '2018-01-01')
).group_by(
    Territory.region,
    func.extract('month', Sales.orderdate)
).all()

# Converter os dados para um DataFrame
data = pd.DataFrame(query, columns=['Region', 'Month', 'Total_Vendas'])

# Pivotar os dados para que as regiões sejam linhas e os meses sejam colunas
heatmap_data = data.pivot_table(index='Region', columns='Month', values='Total_Vendas', fill_value=0)

# Configura o gráfico
plt.figure(figsize=(12, 8))  # Define o tamanho da figura

# Cria um mapa de calor para visualizar as vendas por região e mês
sns.heatmap(
    heatmap_data,  # Dados a serem visualizados
    cmap='YlGnBu',  # Esquema de cores para o mapa de calor
    annot=True,  # Adiciona os valores nas células do gráfico
    fmt='g',  # Formato dos valores exibidos (inteiros)
    cbar_kws={'label': 'Total de Vendas'}  # Rótulo da barra de cores
)

plt.title('Mapa de Calor das Vendas por Região e Mês')  # Título do gráfico
plt.xlabel('Mês')  # Rótulo do eixo X
plt.ylabel('Região')  # Rótulo do eixo Y

# Salvar Gráficos em .png
plt.savefig('.\Gráficos\GraficoDeCalor.png')

# Mostrar o gráfico
plt.show()

