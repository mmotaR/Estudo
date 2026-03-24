# CONDICIONAIS 

#São estruturas que permitem ao nosso programa tomar decisões com base
# em determinadas condições. Em outras palavras, o programa pode executar
# açoes diferentes dependendo de uma situação específica.

# Exemplo

# Você está em uma cafeteria e está com pouco dinheiro.
# O capuccino custa R$ 10 reais, café com leite R$ 7,00 e o café simples R$ 4,00.

#Se você tiver 10 reais ou mais na carteira, pode pedir o capuccino.
# Se tiver entre 7 e 10 reais, pode pedir o café com leite.
# Se não, pode o café simples.

# Sintaxe básica no Python:

# if - "se"
# else - "senão"
# elif - "se + se não"

# if condição:
#     bloco de código a ser executado se a condição for verdadeira
# elif outra_condição: 
#     bloco código executado se a primeira condição for falsa, mas essa for verdadeira. 
# else:
#     bloco de código a ser executado se nenhuma das condições anteriores for verdadeira

# Exemplo prático:

# Verificando a idade para entrada em um evento (18 Anos)

#Código abaixo: 

#idade = int(input("Digite sua idade: ")) #Usuário digita a idade.

#if idade >= 18:
#    print("Você pode entrar no evento.")
#else:
#    print("Desculpe, você não tem idade suficiente para entrar no evento.")

# Verificando a nota de um aluno. 

nota = float(input("Digite sua nota: ")) #Usuário digita a nota.

if nota >= 7:
    print("Parabéns! Você passou de ano.")
elif nota >= 5:
    print("Você está de recuperação. Estude mais e tente novamente.")
else:
    print("Infelizmente, você reprovou. Mas não desista, continue se esforçando e tente novamente no próximo ano!")