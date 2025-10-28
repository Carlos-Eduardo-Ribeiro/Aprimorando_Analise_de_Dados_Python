#Função imprime nome completo
def nomeCompletoIprim (fNome, lNome):
    print(f"Seu nome completo é {fNome} {lNome}. ")

nomeCompletoIprim("Carlos", "Eduardo")

#Função para some dois numeros
def somaDois (num1, num2):
    return num1 + num2

print(somaDois(4,4))

#função  com parânmetro

def morroEm (lugar="Cavaleiro"):
    print(f"Eu morro em {lugar}")

morroEm()

#Função para avaliar um filme

def avaliaFilme (numAvl, nomeFilme):
    total = 0 
    for i in range(numAvl):
        nota = float(input("Digite a nota: "))
        total += nota
    if total > 0:
        media = total/numAvl
    else:
        media = 0
    
    print(f"A média do filme {nomeFilme} é igual a {media}")

avaliaFilme(3, "TOP")