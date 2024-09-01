from tabelas import Calendar, Customer, Product, ProductCategory, ProductSubcategory, Territory, Return, Sales
from BancoDeDados import engine
import pandas

#  A importação é feita utilizando a biblioteca pandas

df = pandas.read_csv('.\Desafio 1\csv\AdventureWorks_Calendar.csv', parse_dates=['Date'])
df.to_sql(con=engine, name=Calendar.__tablename__, if_exists='append', index=False)

df = pandas.read_csv('.\Desafio 1\csv\AdventureWorks_Customers.csv', parse_dates=['BirthDate'], encoding='latin-1')
df.to_sql(con=engine, name=Customer.__tablename__, if_exists='append', index=False)

df = pandas.read_csv('.\Desafio 1\csv\AdventureWorks_Product_Categories.csv')
df.to_sql(con=engine, name=ProductCategory.__tablename__, if_exists='append', index=False)

df = pandas.read_csv('.\Desafio 1\csv\AdventureWorks_Product_Subcategories.csv')
df.to_sql(con=engine, name=ProductSubcategory.__tablename__, if_exists='append', index=False)

df = pandas.read_csv('.\Desafio 1\csv\AdventureWorks_Products.csv')
df.to_sql(con=engine, name=Product.__tablename__, if_exists='append', index=False)

df = pandas.read_csv('.\Desafio 1\csv\AdventureWorks_Territories.csv')
df.to_sql(con=engine, name=Territory.__tablename__, if_exists='append', index=False)

df = pandas.read_csv('.\Desafio 1\csv\AdventureWorks_Returns.csv', parse_dates=['ReturnDate'])
df.to_sql(con=engine, name=Return.__tablename__, if_exists='append', index=False)

df = pandas.read_csv('.\Desafio 1\csv\AdventureWorks_Sales_2015.csv', parse_dates=['OrderDate', 'StockDate'])
df.to_sql(con=engine, name=Sales.__tablename__, if_exists='append', index=False)

df = pandas.read_csv('.\Desafio 1\csv\AdventureWorks_Sales_2016.csv', parse_dates=['OrderDate', 'StockDate'])
df.to_sql(con=engine, name=Sales.__tablename__, if_exists='append', index=False)

df = pandas.read_csv('.\Desafio 1\csv\AdventureWorks_Sales_2017.csv', parse_dates=['OrderDate', 'StockDate'])
df.to_sql(con=engine, name=Sales.__tablename__, if_exists='append', index=False)