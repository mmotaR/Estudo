# Jogo de adivinhação

# No jogo de adivinhação, o usuário precisa adivinhar um número secreto gerado aleatoriamente pelo computador. 
# O programa fornece dicas se o palpite do usuário é muito alto ou muito baixo, 
# e continua até que o usuário acerte o número.
# Ele pode tentar várias vezes até acertar.

import random # A biblioteca random é importada para gerar o número secreto de forma aleatória.

numero_secreto = random.randint(1, 10) # O número secreto é gerado aleatoriamente entre 1 e 10 usando a função randint() da biblioteca random.
tentativa = 0
contador = 0

while tentativa != numero_secreto: # Enquanto a tentativa for diferente do número secreto, o loop continua.
   tentativa = int(input("Tente adivinhar um número de 1 a 10: "))
   contador += 1

   if tentativa < numero_secreto: # Se a tentativa for menor que o número secreto, o programa informa que é muito baixo.
      print("\nO número secreto é maior! Tente novamente.\n") # Se a tentativa for maior que o número secreto, o programa informa que é muito alto.
   elif tentativa > numero_secreto:
      print("\nO número secreto é menor! Tente novamente.\n") # Se a tentativa for igual ao número secreto, o programa parabeniza o usuário por acertar.
   else:
      print(f"\nParabéns! Você acertou o número secreto em {contador} tentativas.\n") # O loop termina quando o usuário acerta o número secreto.