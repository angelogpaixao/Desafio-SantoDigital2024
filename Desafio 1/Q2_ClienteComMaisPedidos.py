from BancoDeDados import Session
from calendar import month_name
from sqlalchemy.sql import func
import pandas as pd
from tabelas import Product, ProductCategory, ProductSubcategory, Sales, Customer, Territory, Return

session = Session()

# Consulta para buscar o cliente com o maior número de pedidos
result = session.query(
    Customer.firstname,  # Seleciona o primeiro nome do cliente
    Customer.lastName,   # Seleciona o sobrenome do cliente
    func.count(Sales.ordernumber)  # Conta o número de pedidos do cliente
).join(
    Customer # Faz uma junção entre a tabela Sales e a tabela Customer
).filter(
    Sales.customerkey == Customer.customerkey  # Filtra para garantir que o cliente corresponde à chave do cliente na tabela Sales
).group_by(
    Sales.customerkey,  # Agrupa os resultados pela chave do cliente
    Customer.firstname  # Inclui o primeiro nome do cliente no agrupamento
).order_by(
    func.count(Sales.ordernumber).desc()  # Ordena os resultados pelo número de pedidos em ordem decrescente
).first()  # Obtém o primeiro resultado da consulta, que será o cliente com o maior número de pedidos

df = pd.DataFrame([result], columns=['firstname', 'lastname', 'orderkey'])
df.to_csv('.\ResultadosCSV\ClienteComMaisPedidos.csv', index=False)