 #Fatorial 

def fatorial(num):
    if num == 1:
        return num
    else:
        return (num * fatorial(num -1))  

numero = int(input("Digite um númrto para o fatotial: "))
print(f"O fatorial  de {numero} é igual a {fatorial(numero)}")

#SomaTotal 

def sum (num):
    if num == 1:
        return num
    else:
        return (num + sum(num - 1))

numero = int(input("Digite um númrto para a soma total: "))
print(f"O soma total  de {numero} é igual a {sum(numero)}")