from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///banco.db", echo = True)
Base = declarative_base()

class Filme(Base):
    ___tablename__ = "filmes"
    id = Column(Integer, primary_key = True)
    nome = Column(String, nullable= False)
    ano = Column(Integer, nullable=False)
    nota = Column(Float, nullable=False)

Base.metadata.create_all(engine)

#inserir dados 
def adiciona_filmes(nome, ano, nota):

    Session =sessionmaker(bind=engine)
    session = Session()
    filme = Filme(nome = nome, ano = ano, nota=nota)
    session.add(filme)
    session.commit()
    session.close()

adiciona_filmes("Verão 2000", 2021, 5.2)
adiciona_filmes("Outono 3500", 2020, 7)
adiciona_filmes("Ineverno  8000", 1999, 8.1)
adiciona_filmes("Primavera", 2002, 9.6)




