# Jogo de adivinhação

# No jogo de adivinhação, o usuário precisa adivinhar um número secreto gerado aleatoriamente pelo computador. O programa fornece dicas se o palpite do usuário é muito alto ou muito baixo, e continua até que o usuário acerte o número.
# Ele pode tentar várias vezes até acertar.

numero_secreto = 10
tentativa = 0

while tentativa != numero_secreto: # Enquanto a tentativa for diferente do número secreto, o loop continua.
   tentativa = int(input("Tente adivinhar um número de 1 a 10:"))
   
   if tentativa < numero_secreto: # Se a tentativa for menor que o número secreto, o programa informa que é muito baixo.
      print("Muito baixo! Tente novamente.") # Se a tentativa for maior que o número secreto, o programa informa que é muito alto.
   elif tentativa > numero_secreto:
      print("Muito alto! Tente novamente.") # Se a tentativa for igual ao número secreto, o programa parabeniza o usuário por acertar.
   else:
      print("Parabéns! Você acertou!") # O loop termina quando o usuário acerta o número secreto.