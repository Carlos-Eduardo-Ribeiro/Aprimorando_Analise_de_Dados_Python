filmes = {
    "titulo" : "Mega Mente",
    "anoLancamento" : 2010,
    "notaFilme" : 9,
    "genero" : ["Avantura", "ficção", "Animação"]
}
print(filmes)
print(len(filmes))
print(type(filmes))

#Recuperar elemento
print(filmes["genero"])
print(filmes.get("notaFilme"))

#buscar apenas as chaves em um dicionário
print(filmes.keys())

#buscar apenas as valores em um dicionário
print(filmes.values()) 

#buscar por chave e valor
print(filmes.items())

#Adicionar itens no dicionario
filmes["titulo"] = "Novo nome"
print(filmes.get("titulo"))

#Update
filmes.update({"anoLancamento" : 2000})
print(filmes.get("anoLancamento"))

#Remover
filmes.pop("anoLancamento")
print(filmes.get("anoLancamento"))