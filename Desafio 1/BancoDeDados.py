from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# Conectando ao banco de dados SQLite chamado 'adventureworks.db'.
engine = create_engine('sqlite:///adventureworks.db', echo=True)

# Cria uma classe Session, que pode ser usada para criar novas sessões de banco de dados.
# Essas sessões são utilizadas para interagir com o banco de dados, como realizar consultas e inserir dados.
Session = sessionmaker(bind=engine)

# Cria uma base para definir as classes.
# As classes que herdam desta base serão automaticamente associadas às tabelas do banco de dados.
Base = declarative_base()



