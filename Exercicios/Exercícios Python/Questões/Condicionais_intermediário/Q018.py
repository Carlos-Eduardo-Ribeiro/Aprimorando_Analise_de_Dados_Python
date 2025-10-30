def categorias (x):
    if(x<12):
        return 'Criança'
    elif(x>=12 and x<18):
        return 'Adolescente'
    elif(x>=18 and x<60):
        return 'Adulto'
    else:
        return 'Idoso'
    
idade = int(input('Digite a sua idade: '))
print(f'Result: {categorias(idade)}')

