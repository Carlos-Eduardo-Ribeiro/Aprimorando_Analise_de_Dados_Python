movieList =["Titanic", "A Orfã", "Piratas do Mar", "Super Guerra"]

#Listando valores menores que 4
for i in range(10):
    if i < 4:
        print(i)

#Com ListComprehension
listNumber = [i for i in range(10) if i < 4]
print(listNumber)

#Filmes com e no nome com ListComprehensione o in 
movieListE = [i for i in movieList if 'e' in i.lower()]
print(movieListE)

#
while True: 
    print("\nBUSCA:\n")
    nomeProcurado = input(f"Digite livro para buscar (ou sair para sair): ")
    if nomeProcurado.lower() ==  "sair":
        print("Busca encerrada.\n")
        break

    listF = [movie for movie in movieList if nomeProcurado.lower() in movie.lower()]

    if listF:
        for i in listF:   
            print(f"Filme: {i} encontrado.")                       
    else:
         print("Filme não encontrado")
