from BancoDeDados import engine
from tabelas import Base

# Cria todas as tabelas no banco de dados que são descritas pelas classes
Base.metadata.create_all(engine)