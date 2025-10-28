filmesSet = {"Filme 1", "Filme 2", "Filme 3",
              "Filme 4", "Filme 5"}

#Tipo do dados
print(type(filmesSet))

#Temanho do set
print(len(filmesSet))

#O set condeça os valores True e 1
#Multiplicidade não importa
emxpleSet = {"Templo", True, 1, 8.7}
print(emxpleSet)

#Adição de itens em uma tupla
filmesSet.update(emxpleSet)
print(filmesSet)
emxpleSet.clear()
print(emxpleSet)

#Removendo itens
filmesSet.remove("Filme 1")
print(filmesSet)