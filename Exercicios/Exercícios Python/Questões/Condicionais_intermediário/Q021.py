import string


def validadorSenha(s):

    alfabetoAlto = string.ascii_uppercase
    alfabetoBaixo = string.ascii_lowercase
    numeros = '0123456789'
    x=y=z=False

    if len(s)>=8:
        for i in range(len(s)):
            if s[i] in alfabetoAlto:
                x=True
            elif s[i] in alfabetoBaixo:
                y=True
            elif s[i] in numeros:
                z=True   
    if x == True and y==True and z==True:
        return 'Ok'
    else:
        return 'Senha invalida'
    
senha = str(input('digite a sua senha: '))
print(f'Result: {validadorSenha(senha)}')
   

