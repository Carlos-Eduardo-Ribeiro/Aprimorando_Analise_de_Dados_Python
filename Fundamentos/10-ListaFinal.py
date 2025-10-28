filmesList = ["Filme 1", "Filme 2", "Filme 3",
              "Filme 4", "Filme 5"]

#Tamanho de um lista
print(len(filmesList))

#Retornando um index pelo item
print(filmesList.index("Filme 1"))

#Adiciolnar um intem um na lista
filmesList.append("Filme 6")
print(filmesList)

#Ordenar uma lista
filmesList.sort()
print(filmesList)

#Copiando uma lista
filmescopy = filmesList.copy()
filmescopy.remove("Filme 5")
print(f"copia da list {filmescopy}")

#Linpar lista
filmescopy.clear()
print(f"copia da list {filmescopy}")

