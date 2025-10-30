def sanatizacao(x):

    novoTexto = x.replace('¡', '&lt').replace('¿', '&gt;')

    if(novoTexto==x):
        return f'Texto inalterado: {x} -> {novoTexto}'
    else:
        return f'Texto alterado: {x} -> {novoTexto}'

texto = str(input('Digite o texto: '))
print(f'Result: {sanatizacao(texto)}')

        