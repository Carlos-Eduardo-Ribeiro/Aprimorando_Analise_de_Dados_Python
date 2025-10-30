def conversorTemperatura ():
    lista = []
    for i in range(3):
        if(i<1):
         valor = float(input('Digite a temperatura: '))
         lista.append(valor)
        else:
         valor = str(input('Digite a unidade de temperatura: '))
         lista.append(valor.lower())

    if(isinstance(lista[0], float) and lista[1]=='c' and lista[2]=='f'):
        resultado = round(lista[0] * 1.8 + 32, 2)
    elif(isinstance(lista[0], float) and lista[1]=='f' and lista[2]=='c'):
        resultado = round((lista[0]-32)/1.8, 2)
    else: 
        resultado = 'Valor invalido'

    return resultado
    
print(f'result: {conversorTemperatura()}')


