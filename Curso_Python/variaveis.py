# Variáveis e tipos de dados "básicos"

# Variáveis são usadas para armazenar informações que podem ser usadas e manipuladas em um programa. 
# Em Python, as variáveis não precisam ser declaradas com um tipo específico, pois o Python é uma linguagem de tipagem dinâmica. 
# Isso significa que você pode atribuir diferentes tipos de dados a uma variável ao longo do tempo.

# Exemplo de variáveis com diferentes tipos de dados:

nome = "Matheus"  # String (texto)
idade = 30      # Inteiro (número inteiro) 
altura = 1.65   # Float (número decimal)
dev = True      # Booleano (verdadeiro ou falso)

# print(f"Olá, {nome}! Você tem {idade} anos, sua altura é {altura} metros, e é um desenvolvedor: {dev}.")

nome = input("Digite seu nome:") # A função input() é usada para obter entrada do usuário. O valor digitado pelo usuário será armazenado na variável "nome".
idade = int(input("Digite a sua idade:")) # A função int() é usada para converter a entrada do usuário em um número inteiro, já que a função input() retorna uma string por padrão.
altura = float(input("Digite a sua altura:")) # A função float() é usada para converter a entrada do usuário em um número decimal.

print(f"Olá, {nome}! Você tem {idade} anos e sua altura é de: {altura} metros.")