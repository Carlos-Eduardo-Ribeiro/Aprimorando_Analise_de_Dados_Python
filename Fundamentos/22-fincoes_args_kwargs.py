# Usamos o args para definir um quantitoo não sebido de argumentos que uma função pode ter

def soma(*num):
    sum_total = 0
    for i in num:
        sum_total += i
    print(f"A soma é {sum_total}")

soma(7)
soma(7,9) # (0, 7), (1, 9) 
soma(2,4,6) # (0, 2), (1, 4), (2, 6) 

'''
O args vai subentender os dados como uma tupla (posição, valor) 
e vai andar por ela, interando os valores. O args permite um número
literalmente de infinito de valores.
'''

# Usamos Kwargs para Alaem dos valores podemos passa as chaves para cada argumento

def cursos (**data):
    print("\nLista de Cursos:\n")
    for key, values in data.items():
        print(f"key: {key}\nvalue: {values}\n")

cursos(nome="Python", category="Backend", level="Iniciante")

'''
O kwargs igualmente ao args, vai passa um número ilimitado de 
argumentos, porem diferentemente o args, vai passa uma estrutura 
similar a um dicionário, com chave valor (chave = "valor"), é 
tipo um enumerate, mas invez de retornar o index, reorna a chave e
o valor correspondente, além de usufruir de capacidade de receber um 
número inimitado de valores.
'''