import sqlite3  as sql3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "titulo.db")

#Gerar a conexão com o banco
def conectar_bd():
     
     banco = sql3.connect(DB_PATH)
     return banco


# Inserir dados no banco
def insere_dados(nome, ano, nota):

    conexao =  conectar_bd()
    cursor =  conexao.cursor()

    cursor.execute(
    """
        INSERT INTO filmes(nome, ano, nota)
        VALUES(?, ?, ?);                       
    """, (nome, ano, nota)
        )
    conexao.commit()
    conexao.close()


# Listar dados 
def listar_dados():

    conexao = conectar_bd()
    cursor =  conexao.cursor()

    dados = cursor.execute("""SELECT * FROM filmes""")
    dados = dados.fetchall()

    conexao.close()

    return dados