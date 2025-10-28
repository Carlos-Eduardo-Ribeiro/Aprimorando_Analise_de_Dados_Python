# nome = input("Digite o nome do Filme: ")
# anoLancamento = int(input("\nDigite o ano de lançamento do Filme: "))
# nota = float(input("\nDigite a nota do Filme: "))

# #verifiacar se é recomendado

# if nota >= 9.0 and anoLancamento > 2015:
#     print(f"Filme {nome}, é muito bom, recomendo.")
# else: 
#     print(f"O filme {nome}, não recebel uma boa nota.")

num1 = float(input("Digite o valor 1: "))
num2 = float(input("Digite o valor dois: "))
operation = input("Digite a operação a ser realizada: (+ - * /): ")

if operation == "+":
    print(f"O valor da soma é {num1+num2}")
elif operation == "-":
    print(f"O valor da subtração é {num1-num2}")
elif operation == "*":
    print(f"O valor da multiplocação é {num1*num2}")
elif operation == "/":
    if num2 == 0:
        print(f"Número {num2} precisa ser diferente de zero.")
    else:
        print(f"O valor da divisão é {num1/num2}")
else:
    print(f"Valor {operation:.2f} não está detro dos parâmetros.")
    
