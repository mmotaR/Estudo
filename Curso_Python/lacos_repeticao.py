# Laços de Repetição (for e while)

# Imagine que você precisa pedir para alguém contar de 1 a 100.
# e escrever cada número em um papel. Fazer isso manualmente
# seria muito cansativo e demorado, né ?

# Agora, imagine que um programa pode fazer essa contagem automaticamente,
# sem precisar repetir o mesmo comando 100 vezes. É examamente isso 
# que os laços de repetição fazem !

# Os laços de repetição são usados para executar um bloco de código 
# várias vazes, até que uma condição seja atingida.

# Python tem dois tipos principais de laços de repetição:

# for Quando sabemos quantas vezes queremos repetir algo.
# while Quando queremos repetir algo até que uma condição se torne falsa.

# FOR 

# o For é usando quando sabemos quantas vezes queremos repetir um bloco de código.
# Ele percorre uma sequência de valores, como uma lista , um intervalo de número 
# ou até mesmo letras de uma palavra.

# Estrutura: 

#for variavel in sequência:
    # Código a ser repetido.

# Contando de 1 a 5 com o For: 

# (1, 2, 3, 4, 5)

for numero in range(1, 51):
   print(numero)

# O range (1, 6) gera uma sequência de números de 1 a 5 (o 6 não é incluído).

# Percorrendo um lista de compras

compras = ["leite", "pão", "ovos", "frutas"]

for item in compras:
   print(f" comprar: {item}")

# Percorrendo as letras de uma palavra

palavra = "Python"

for letra in palavra:
   print(letra)

# While 

# O while é usando quando não sabemos 
# quantas vezes a repetição vai acontecer,
# mas sabemos a condição que deve ser atendida para continuar.

# while condição:
#   # Código a ser repetido enquanto a condição for verdadeira.

# obs: Cuidado com loops infinitos !
# Se a condição nunca mudar para false, o código nunca para de rodar. 

# Contagem regressiva com while:

contador = 5

while contador > 0:
    print(contador)
    contador -= 1 # Diminuindo 1 do contador a cada repetição;

print ("Fogo !")

# Pedindo senha até acertar:

senha_correta = "1234"
senha = ""

while senha != senha_correta:
    senha = input("Digite a senha:")

print("Acesso concedido !")