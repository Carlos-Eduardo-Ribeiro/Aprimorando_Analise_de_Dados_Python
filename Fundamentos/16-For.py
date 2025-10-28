movieList =["Titanic", "A Orfã", "Piratas do Mar", "Super Guerra"]
print(movieList)

#Interando com for uma lista
for movie in movieList:
    if movie != "Titanic":
        print(movie)

#Usando o break para para o laçõ sobre uma condição
for m in movieList:
    if m[0] == "A":
        break
    else:
        print(m)

#Como pular um interação no for
for movie in movieList:
    if movie[0] == "T":
        continue
    print(movie)

#- Avaliaçõ do filme

nome = input("\nDigite o nome do filme: ")
nota = int(input("Digite quantas avaliações do filme voce quer fazer: "))

total = 0

for i in range(nota):
    notes = float(input("Digite a nota para o filme:"))
    total += notes

if nota > 0:
    media = total/nota
else:
    media = 0

print(f"A nota média é igual a {media:.2f}\n")

    