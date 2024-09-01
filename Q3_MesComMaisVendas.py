from BancoDeDados import Session
from calendar import month_name
from sqlalchemy.sql import func
import pandas as pd
from tabelas import Product, ProductCategory, ProductSubcategory, Sales, Customer, Territory, Return

session = Session()

# Consulta para buscar o mês do ano em que ocorrem mais vendas
result = session.query(
    func.extract('month', Sales.orderdate).label('Mês'),  # Extrai o mês da data do pedido e o rotula como 'Mês'
    func.sum(Sales.orderquantity * Product.productprice).label('Total_vendido')  # Calcula o total vendido (quantidade * preço do produto) e o rotula como 'Total_vendido'
).join(
    Product  # Faz uma junção com a tabela Product
).group_by(
    func.extract('month', Sales.orderdate)  # Agrupa os resultados por mês
).order_by(
    func.sum(Sales.orderquantity * Product.productprice).desc()  # Ordena os resultados pelo total vendido em ordem decrescente
).first()  # Obtém o primeiro resultado da consulta, que será o mês com o maior total vendido

# Montar o nome do mês a partir do número
month_name = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho',
                  7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}
mes = month_name.get(int(result[0]))

# Criar o DataFrame e salvar como CSV
df = pd.DataFrame([{
    'mes': mes,
    'total_vendido': result[1]
}])

df.to_csv('.\ResultadosCSV\MesComMaisVendas.csv', index=False)