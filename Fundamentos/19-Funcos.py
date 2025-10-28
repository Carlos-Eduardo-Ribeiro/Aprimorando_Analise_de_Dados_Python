#Função para inpressão

nome = input("\nDigite o seu nome: ")
def welcome(nome):
    print(f"Bem vindo {nome}")
for i in range(10):
    welcome(nome)

#Função para calcular média de notas

def mediaNotas():
    numNotas = int(input("Digite a qtd nota: "))
    total = 0

    for i in range(numNotas):
        nota = float(input("Digite a nota correspondente: "))
        total += nota
    if total > 0:
        media = total/numNotas
    else:
        media = 0

    return media

movieList =["Titanic", "A Orfã", "Piratas do Mar", "Super Guerra"]

# print(mediaNotas())

def CadastroFilme ():
    nome = input(f"Digite o nome para cadastro: ")
    
    for i in movieList:
        if i != nome:
            movieList.append(nome)
            return True
        else:
            return False
        
print(CadastroFilme())

print(movieList)