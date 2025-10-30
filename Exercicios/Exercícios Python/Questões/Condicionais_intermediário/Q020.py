def maiorDe3 ():
    
    lista = []
    for i in range(3):
        valor = int(input(f'digite o valor {i+1}: '))
        lista.append(valor)
    
    lista.sort()

    return f'Menor valor {lista[0]}, Maior valor: {lista[-1]}'

print(f'Result: {maiorDe3()}') 