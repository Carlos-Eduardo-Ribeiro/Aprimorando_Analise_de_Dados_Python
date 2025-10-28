nomeFilme = "Top Gun"

descricaoFilme = '''mrcimicrmicnrnrcnnrnrcn
mrncnrjcnnrnjcnj,nrnrnrunr,unujn'''

#Letras maúsculas e menúsculas
print(nomeFilme.upper())
print(nomeFilme.lower())

#Primeira letra maúsculas
print(descricaoFilme.capitalize())

#Primeira letra cada linha maúsculas
print(descricaoFilme.title())

#Retorna um string cetralizada
print(nomeFilme)
print(nomeFilme.center(10, '-'))

#Retorna posição com indise
print(nomeFilme.find("n"))

#Contar número de letras em uma função
print(nomeFilme.count("n"))
print(descricaoFilme.count("n"))

#Subistituição
print(nomeFilme.replace("T", "X"))

#Quebrando linhas em uma String com split
print(descricaoFilme.split(','))




