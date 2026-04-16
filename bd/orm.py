from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

enngine = create_engine("sqlite:///bd/banco.db", echo=True)
Base =  declarative_base()

# Convertendo uma class declarada em uma tabela usando ORM
class Filmes(Base):
    __tablename__ = "filmes"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    nota = Column(Float, nullable=False)

Base.metadata.create_all(enngine)

# Usando oORM para inserir um registro
def inserir_filme(nome, ano, nota):
    Sessino = sessionmaker(bind=enngine)
    session = Sessino()
    filme = Filmes(nome=nome, ano=ano, nota=nota)
    session.add(filme)
    session.commit()
    session.close()

def listar_filme(id):
    Session = sessionmaker(bind=enngine)
    session = Session()
    filme = session.query(Filmes).filter_by(id=id).first()
    session.close()
    return filme

# Usando IRM para atualizar um registro
def atualizar_filme(id, nome=None, ano=None, nota=None):
    Sessino = sessionmaker(bind=enngine)
    session =  Sessino()
    filme = session.query(Filmes).filter_by(id=id).first()
    if filme:
        if nome is not None:
            filme.nome = nome
        if ano is not None:
            filme.ano = ano
        if nota is not None:
            filme.nota = nota
        session.commit()
    session.close()


# Usando orm para esxcluir um registro
def excluir_filme(id):
    Session = sessionmaker(bind=enngine)
    session = Session()
    filme = session.query(Filmes).filter_by(id=id).first()
    if filme:
        session.delete(filme)
        session.commit()
    session.close()

# # CREATE
# inserir_filme("O grito", 1999, 7.2)
# inserir_filme("O Voo", 2010, 8.2)
# inserir_filme("O Demolidor", 1998, 6.9)

# # UPDATE
# atualizar_filme(2, "Novo nome", 1000, 10)

# # DELETE
# excluir_filme(2)