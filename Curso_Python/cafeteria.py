# Pede ao usuário que digite quanto dinheiro ele tem.
# O input sempre retorna uma string, então usamos float() 
# para converter para número decimal.

dinheiro = float(input("Quanto tenho na carteira R$ ?\n"))

# Verifica se o valor é maior ou igual a 10.
# Se for, essa condição é verdadeira
# e o bloco abaixo é executado.

if dinheiro >= 10:
    print("Você pode pedir um capuccino.")

# Caso a condição acima seja falsa, o programa testa esta.
# Aqui verificamos se o dinheiro é maior ou igual a 7.

elif dinheiro >= 7:
    print("Você pode pedir um café com leite.")

# Se nenhuma das condições anteriores for verdadeira,
# o programa executa o bloco do else.
else:
    print("Você pode pedir um café preto")