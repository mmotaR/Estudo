# Listas e Tuplas 

# Tipos de dados que armazenam múltiplos valores,
# mas têm diferenças importantes.

# Listas: 
# - Modificável (pode adicionar, remover e alterar valores)
# - Mais lenta 
# - Quando precisamos modificar dados

# Tuplas:
# - Não é modificável (uma vez criada, não pode ser alterada)
# - Mais rápida 
# - Quando os dados não devem ser alterados

# Lista
# Definida entre colchetes [] e pode armazenar
# diferentes tipos de dados.

frutas = ["maçã", "banana", "laranja"]
numeros = [1, 2, 3, 4, 5]
mistura = ["python", 3.14, True]

# Acessando elementos da lista

print(frutas[0]) # Saída: "maçã"
print(frutas[1]) # Saída: "banana"
print(frutas[2]) # Saída: "laranja"
print(frutas[-1]) # Saída: "laranja" (indice negativo conta de três para frente)

# alterando um valor na lista 
# print(frutas) 

frutas[1] = "uva"
print(frutas) # Saída: ["maçã", "uva", "laranja"]

# Adicionando elementos à lista

# append(): Adiciona um elemento ao final da lista.
# insert(): Adiciona um elemento em uma posição específica.

numeros = [1, 2, 3]
print(numeros) # Saída: [1, 2, 3]   

numeros.append(4)
print(numeros) # Saída: [1, 2, 3, 4]

numeros.insert(1, 10) # (posição, valor)
print(numeros) # Saída: [1, 10, 2, 3, 4] (inseriu a 10 na posição 1)

# Removendo elementos da lista

# remove(): # remove um item pelo valor.
# pop(): # remove um item pelo índice (ou o último item se nenhum índice for passado).

frutas = ["maçã", "banana", "laranja", "uva"]
frutas. remove("banana")
print(frutas) # Saída: ["maçã", "laranja"]

frutas.pop(0) # remove o item na posição 0 (maçã)
print(frutas) # Saída: ["laranja"]


frutas.pop() # remove o último item (uva)
print(frutas) # Saída: [] (lista vazia)

# Tuplas
# Tuplas são como listas, mas imutáveis. Elas são criadas como paranteses ().

cores = ("vermelho", "azul", "verde")
numeros = (1, 2, 3, 4, 5)

# Acessando elementos da tupla

print(cores[0]) # Saída: "vermelho"
print(cores[-1]) # Saída: "verde"

# Tentando modificar uma tupla (Erro !)
# cores[1] = "amarelo" # Erro isso gera um erro porque tuplas são imutáveis.

# Convertendo entre listas e tuplas
# Podemos converter uma tupla para uma lista e modificar os elementos.

tuplas = (1, 2, 3)
lista = list(tuplas) # Converte a tupla para uma lista
lista.append(4) # Modifica a lista
tupla = tuple(lista) # Converte a lista de volta para uma tupla
print(tupla) # Saída: (1, 2, 3, 4)

# Quando usar listas ou tuplas?
# - Quando queremos garantir que os dados não sejam alterados.
# - Para armazenar dados fixos como coordenadas, meses do ano, dias da semana, etc.

meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho")
print(meses[2]) # Saída: ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho")