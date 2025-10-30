usuario = 'admin'
senha = '1234'

def login(x, y):
    if(x == usuario and y == senha):
        return 'Login efetuado'
    else:
        return 'Usuário invsalido ou não encontrado'

usuarioInput = str(input('Digite o seu login: '))
senhaInput = str(input('Diagite a sua senha: '))

print(f'Login Result: {login(usuarioInput, senhaInput)}')
