def ordenador(x):
    lista = []
    for i in range(x):
        valor = int(input(f'Digiate o valor {i+1}: '))
        lista.append(valor)
    lista.sort()
    return  lista

numero = int(input(f'Digite quantos números deseja inserir:'))
print(f'Result: {ordenador(numero)}')

