from BancoDeDados import Session
from calendar import month_name
from sqlalchemy.sql import func
import pandas as pd
from tabelas import Product, ProductCategory, ProductSubcategory, Sales, Customer, Territory, Return

session = Session()

# Faturamento total por mês ao longo do último ano

# Consulta para buscar os vendedores que tiveram vendas com valor acima da média no último ano fiscal 
# e também tiveram um crescimento de vendas superior a 10% em relação ao ano anterior

# Calcular a média de vendas do último ano fiscal (exemplo: 2017)
# Calcula a soma total das vendas e divide pelo número de meses (12)
average_sales = session.query(
    func.sum(Sales.orderquantity)
).filter(
    (Sales.orderdate >= '2017-01-01') &
    (Sales.orderdate < '2018-01-01')
).scalar() / 12  # Supondo que estamos calculando a média mensal

# Calcular o total de vendas e filtrar os vendedores com vendas acima da média
result = session.query(
    Territory.country,
    Territory.region,
    func.sum(Sales.orderquantity).label('total_vendido')
).join(
    Sales
).filter(
    (Sales.orderdate >= '2017-01-01') &
    (Sales.orderdate < '2018-01-01')
).group_by(
    Territory.country,
    Territory.region
).having(
    func.sum(Sales.orderquantity) > average_sales
).subquery()

# Calcular as vendas do ano anterior (exemplo: 2016) para comparação
previous_year_sales = session.query(
    Territory.country,
    Territory.region,
    func.sum(Sales.orderquantity).label('prev_total_vendido')
).join(
    Sales
).filter(
    (Sales.orderdate >= '2016-01-01') &
    (Sales.orderdate < '2017-01-01')
).group_by(
    Territory.country,
    Territory.region
).subquery()

# Calcular o crescimento das vendas e filtrar os vendedores com crescimento superior a 10%
growth_query = session.query(
    result.c.country,  # Seleciona o país da subconsulta
    result.c.region,   # Seleciona a região da subconsulta
    result.c.total_vendido,  # Seleciona o total vendido no último ano fiscal
    previous_year_sales.c.prev_total_vendido,  # Seleciona o total vendido no ano anterior
    (result.c.total_vendido / previous_year_sales.c.prev_total_vendido - 1).label('growth')  # Calcula o crescimento percentual
).join(
    previous_year_sales,  # Junta a subconsulta de vendas do ano anterior
    (result.c.country == previous_year_sales.c.country) &  # Condição de junção pelo país
    (result.c.region == previous_year_sales.c.region)  # Condição de junção pela região
).filter(
    (result.c.total_vendido / previous_year_sales.c.prev_total_vendido - 1) > 0.10  # Filtra crescimento superior a 10%
).all()  # Executa a consulta e retorna todos os resultados

# Convertendo o resultado da consulta para um DataFrame
df = pd.DataFrame(growth_query, columns=[
    'Country', 
    'Region', 
    'Total_Vendido', 
    'Prev_Total_Vendido', 
    'Growth'
])

# Salvando o DataFrame como um arquivo CSV
df.to_csv('.\ResultadosCSV\MaioresVendasPorRegiao.csv', index=False)