movieList =["Titanic", "A Orfã", "Piratas do Mar", "Super Guerra"]
print(len(movieList))

#Interando valores com While
index = 0 
while index < len(movieList):
    print(movieList[index])  
    index += 1 

#Interando valores com While e break
index = 0 
while index < len(movieList):
    if movieList[index] == "A Orfã":
        break
    else:
         print(movieList[index])  
         index += 1 

#Interando valores com While e continue
index = 0 
while index < len(movieList):
    if movieList[index] == "A Orfã":
        index += 1 
        continue
    print(movieList[index])  
    index += 1 

#Exemplo
nome = input("\nDigite o nome do filme: ")
nota = int(input("Digite quantas avaliações você quer: "))
index3 = 0
total = 0

while index3 < nota:
    notas = float(input(f"Digite a nota: "))
    total +=notas
    index3 +=1

if nota > 0:
    media = total/nota
else:
    media = 0
    print(f"média: {media:.2f}")

print(f"A nota é igual à {media:.2f}")



