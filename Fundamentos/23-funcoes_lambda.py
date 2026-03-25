# LAMBDA

# Função que eleva valores ao quadrado
power =  lambda x : x ** 2
print(power(2))

# Função que verifica de um número é par
e_par =  lambda x : x % 2 == 0 # Posso fazer uma comparação True/False
print(e_par(3))
print(e_par(2))

# Função que divide um número por outro
div = lambda x, y : x/y # Posso passa mas de um parmêtro
print(div(20,5))

# Verificando se os valores são números ou não
e_num =  lambda x : True if isinstance(x,(int, float, complex)) else False
print(e_num(2))
print(e_num("oi"))

# Função que reverte uma string
reverse_str = lambda x : x[::-1]
print(reverse_str("Carlos"))

# Média de filmes
lista_filmes = ["Batiman", "Duna", "Bem 10"]

dic_filmes = {
    "Batiman" : [9.2, 7, 8.4],
    "Duna": [10, 9.2, 3.5],
    "Bem 10" : [8.2, 4, 7.3] 
}

nota_media =  lambda x : sum(dic_filmes.get(x)) / len(dic_filmes.get(x))
print(nota_media("Batiman"))

# Verificando se está na lista
existe =  lambda x : True if x in dic_filmes else False
print(existe("Batiman"))

# Função de recomendação de filmes com base na nota média
recomend_movie =  lambda x : print(f"Remendo o filme {x} com média {nota_media(x):.2f}")
recomend_movie("Batiman")

