# Cria uma variável chamada 'palavra' e guarda o texto "Python"
palavra = "Python"

# Percorre cada letra da palavra, uma por vez
for letra in palavra:
    
    # Verifica se a letra atual é igual a "y"
    if letra == "y":
        
        # Se for "y", mostra a mensagem na tela
        print("Essa palavra tem a letra Y!")

# Cria uma variável chamada 'palavra' e guarda o texto "matheus mota"
palavra = "matheus mota"
letra_procurada = "m" #Constante

# # Percorre cada letra da palavra, uma por vez.
for letra in palavra:
    
    # Verifica se a letra atual é igual a "m"
    if letra == letra_procurada:
        
        # Se for "y", mostra a mensagem na tela
        print("Essa palavra tem a letra", letra_procurada)
        
        # Para o loop para não repetir a mensagem
        break