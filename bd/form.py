import streamlit as st
import pandas as pd
from dados import*

st.markdown("# Filmania")
st.markdown("## Avalie o filme")

# Inputs
nome = st.text_input("Nome do filmes")
ano = st.number_input("Ano do Filme:", min_value=2012, max_value=2026)
nota =  st.slider("Nota:", min_value=0, max_value=10) 

# Conversões de tipos
nome =  nome.strip()
ano  = int(ano)
nota = float(nota)

# Botões
botao =  st.button("Enviar")

st.write(nome, ano, nota)

if botao:
    if nome == "":
        st.error("Campo nome esta Vazio!")       
    else:
        st.success("Filme Cadastrado com Sucesso")
        insere_dados(nome, ano, nota)

filmes =  listar_dados()
st.markdown("## Lista de filmes")
st.table(filmes)