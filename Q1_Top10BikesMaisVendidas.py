from BancoDeDados import Session
from calendar import month_name
from sqlalchemy.sql import func
import pandas as pd
from tabelas import Product, ProductCategory, ProductSubcategory, Sales, Customer, Territory, Return
import matplotlib.pyplot as plt

session = Session()

# Consulta para buscar a quantidade vendida e lucro gerado por produto
result = session.query(
    Sales.productkey,  # Seleciona a chave do produto
    Product.productname,  # Seleciona o nome do produto
    func.sum(Sales.orderquantity).label('total_vendido'),  # Calcula a soma da quantidade de pedidos e rotula como 'total_vendido'
    func.sum((Sales.orderquantity * (Product.productprice - Product.productcost))).label('lucro')  # Calcula o lucro (quantidade * (preço - custo)) e rotula como 'lucro'
).join(
    Product  # Faz uma junção com a tabela Product
).join(
    ProductSubcategory  # Faz uma junção com a tabela ProductSubcategory
).join(
    ProductCategory  # Faz uma junção com a tabela ProductCategory
).filter(
    ProductCategory.categoryname == 'Bikes'  # Filtra para incluir apenas produtos na categoria 'Bikes'
).group_by(
    Sales.productkey,  # Agrupa os resultados pela chave do produto
    Product.productname  # Inclui o nome do produto no agrupamento
).order_by(
    func.sum(Sales.orderquantity).desc()  # Ordena os resultados pela quantidade total vendida em ordem decrescente
).limit(10).all()  # Limita os resultados aos 10 produtos mais vendidos e obtém todos os resultados

df = pd.DataFrame(result, columns=['productkey', 'productname', 'total_vendido', 'lucro'])
df.to_csv('.\ResultadosCSV\Top10BikesMaisVendidas.csv', index=False)

# Cria um dicionário com os dados para o gráfico
data = {
    'ProductName': [r[1] for r in result],   # Nome do produto
    'TotalVendido': [r[2] for r in result],  # Quantidade total vendida
    'Lucro': [r[3] for r in result]          # Lucro gerado
}

# Cria um DataFrame a partir do dicionário
df = pd.DataFrame(data)

# Configurando o gráfico
fig, ax1 = plt.subplots(figsize=(8, 4))

# Gráfico de barras para 'Total Vendido'
ax1.bar(df['ProductName'], df['TotalVendido'], color='b', label='Total Vendido')  # Plota as barras para a quantidade vendida
ax1.set_xlabel('Produto')  # Define o rótulo do eixo X
ax1.set_ylabel('Quantidade Vendida', color='b')  # Define o rótulo do eixo Y e a cor dos rótulos
ax1.tick_params(axis='y', labelcolor='b')  # Define a cor dos rótulos do eixo Y

# Adicionando um segundo eixo Y para o 'Lucro'
ax2 = ax1.twinx()  # Cria um segundo eixo Y que compartilha o mesmo eixo X
ax2.plot(df['ProductName'], df['Lucro'], color='r', marker='o', label='Lucro')  # Plota a linha para o lucro
ax2.set_ylabel('Lucro Gerado', color='r')  # Define o rótulo do segundo eixo Y e a cor dos rótulos
ax2.tick_params(axis='y', labelcolor='r')  # Define a cor dos rótulos do segundo eixo Y

# Rotacionar os nomes dos produtos para melhor visualização
ax1.set_xticklabels(df['ProductName'], rotation=60, ha='right', fontsize=8)  # Rotaciona os rótulos do eixo X para melhor visualização e ajusta a fonte

# Título do gráfico
plt.title('Top 10 Produtos Mais Vendidos (Bicicletas) e Lucro Gerado')  # Define o título do gráfico

# Ajusta o layout para não cortar elementos
plt.tight_layout() 

# Salvar Gráficos em .png
plt.savefig('.\Gráficos\Top10BikesMaisVendidas.png')

# Mostrando o gráfico
plt.show()

