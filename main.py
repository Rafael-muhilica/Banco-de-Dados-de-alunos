from sqlalchemy import create_engine,  Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
db = create_engine("sqlite:///BancoDados.db")
Session = sessionmaker( bind = db)
session = Session()
Base = declarative_base()
class Dado(Base):
         __tablename__ = "dados"
         id = Column( Integer, primary_key=True, autoincrement = True)
         nome = Column( String)
         idade = Column( Integer)
         turma = Column( String)
         def __init__(self, nome, idade, turma):
           self.nome = nome
           self.idade = idade
           self.turma = turma      
Base.metadata.create_all( bind = db)
Dados_estudante = Dado(nome= "Rafael Muhilica", idade = 21,turma="LCC1TB")
Dados_estudante2 = Dado(nome= "Aires Muhilica", idade = 19,turma="LCC1TB")
session.add(Dados_estudante)
session.add(Dados_estudante2)
session.commit()