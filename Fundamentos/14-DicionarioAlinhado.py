import pprint 

dicionarioFilmes = {
    
    "Mega Mente" :{
    "anoLancamento" : 2010,
    "notaFilme" : 9,
    "genero" : ["Avantura", "ficção", "Animação"]
    },
     "O Pianista" :{
    "anoLancamento" : 2019,
    "notaFilme" : 9.8,
    "genero" : ["Avantura", "ficção", "Animação"]
    },
     "War 40k" :{
    "anoLancamento" : 1999,
    "notaFilme" : 10,
    "genero" : ["Avantura", "Guerra", "Animação"]
    }
}

print(dicionarioFilmes,"\n")

#Usando pprint biblioteca
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(dicionarioFilmes)

#Buscando
print(dicionarioFilmes["Mega Mente"]["notaFilme"])


#adicionando novo item
dicionarioFilmes["Mega Mente"]["anoLancamento"]=2045
print(dicionarioFilmes["Mega Mente"]["anoLancamento"])

#Remover
del dicionarioFilmes["Mega Mente"]

pp1 = pprint.PrettyPrinter(depth=4)

pp1.pprint(dicionarioFilmes)