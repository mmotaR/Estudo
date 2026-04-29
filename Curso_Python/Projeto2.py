# Simulador um caixa eletrônico 

# O caixa eletrônico tem as seguintes funcionalidades:
# - Consultar saldo
# - Sacar dinheiro
# - Depositar dinheiro

import datetime # Importa a biblioteca datetime para exibir a data e hora atual

saldo = 1000.0 # Saldo inicial do usuário
extrato = [] # Lista para armazenar o extrato das operações realizadas
saques_realizados = 0 # Contador para limitar o número de saques diários
limite_saques = 3 # Limite de saques diários

print("Bem-vindo ao caixa eletrônico !")

while True: # Loop infinito para o usuário escolher as opções

    print("\nQual operação deseja realizar ?\n")
    print("1- Consultar saldo")
    print("2- Sacar dinheiro")
    print("3- Depositar dinheiro")
    print("4- Consultar extrato")
    print("5- Sair")

    opcao = int(input("\nEscolha uma opção: ")) # O usuário escolhe a opção desejada
    if opcao == 1: # Consultar saldo
        print(f"\nSeu saldo é: R${saldo:.2f}")

    elif opcao == 2: # Sacar dinheiro
        if saques_realizados >= limite_saques: # Verifica se o usuário já atingiu o limite de saques diários
            print("Limite de saques diários atingido !")
        else: # Volta para o início do loop para o usuário escolher outra opção
            valor = float(input("Digite o valor que deseja sacar: R$ "))
            if valor <= 0: # Verifica se o valor a ser sacado é válido
                print("Valor inválido ! Digite um valor maior que zero.")
            elif valor > saldo: # Verifica se o valor a ser sacado é maior que o saldo disponível
                print("Saldo insuficiente !")
            else: # Volta para o início do loop para o usuário escolher outra opção
                saldo = saldo - valor
                saques_realizados += 1  
                print(f"Saque realizado ! Novo saldo: R${saldo:.2f}")
                data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") # Obtém a data e hora atual formatada
                extrato.append(f"{data_hora} | Saque: R${valor:.2f} | Saldo: R${saldo:.2f}") # Adiciona a operação ao extrato

    elif opcao == 3: # Depositar dinheiro
        valor = float(input("Digite o valor que deseja depositar: R$"))
        if valor <= 0: # Verifica se o valor a ser depositado é válido
            print("Valor inválido ! Digite um valor maior que zero.")
        else: # Volta para o início do loop para o usuário escolher outra opção
            saldo = saldo + valor
            print(f"Depósito realizado ! Novo saldo: R${saldo:.2f}")
            data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") # Obtém a data e hora atual formatada
            extrato.append(f"{data_hora} | Depósito: R${valor:.2f} | Saldo: R${saldo:.2f}") # Adiciona a operação ao extrato

    elif opcao == 4: # Consultar extrato
        if not extrato: # Verifica se o extrato está vazio
            print("\nNenhuma operação realizada ainda !")
        else: # Exibe o extrato das operações realizadas
            print("\nExtrato das operações realizadas:")
            for item in extrato:
                print(item)


    elif opcao == 5: # Sair
        print("\nObrigado por usar o caixa eletrônico !\n")
        break # Encerra o loop e sai do programa
    else: # Opção inválida
        print("\nOpção inválida ! Por favor, escolha uma opção válida entre 1 e 5.\n")
    