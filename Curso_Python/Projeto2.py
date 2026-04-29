# Simulador um caixa eletrônico 

# O caixa eletrônico tem as seguintes funcionalidades:
# - Consultar saldo
# - Sacar dinheiro
# - Depositar dinheiro

saldo = 1000.0 # Saldo inicial do usuário

while True: # Loop infinito para o usuário escolher as opções

    print("\nQual operação deseja realizar ?\n")
    print("1- Consultar saldo")
    print("2- Sacar dinheiro")
    print("3- Depositar dinheiro")
    print("4- Sair")

    opcao = int(input("\nEscolha uma opção: ")) # O usuário escolhe a opção desejada
    if opcao == 1: # Consultar saldo
        print(f"\nSeu saldo é: R${saldo:.2f}")

    elif opcao == 2: # Sacar dinheiro
        valor = float(input("Digite o valor que deseja sacar: R$ "))
        if valor <= 0: # Verifica se o valor a ser sacado é válido
            print("Valor inválido ! Digite um valor maior que zero.")
        elif valor > saldo: # Verifica se o valor a ser sacado é maior que o saldo disponível
            print("Saldo insuficiente !")
        else: # Volta para o início do loop para o usuário escolher outra opção
            saldo = saldo - valor
            print(f"Saque realizado ! Novo saldo: R${saldo:.2f}")

    elif opcao == 3: # Depositar dinheiro
        valor = float(input("Digite o valor que deseja depositar: R$"))
        if valor <= 0: # Verifica se o valor a ser depositado é válido
            print("Valor inválido ! Digite um valor maior que zero.")
        else: # Volta para o início do loop para o usuário escolher outra opção
            saldo = saldo + valor
            print(f"Depósito realizado ! Novo saldo: R${saldo:.2f}")

    elif opcao == 4: # Sair
        print("\nObrigado por usar o caixa eletrônico !\n")
        break # Encerra o loop e sai do programa
    else: # Opção inválida
        print("\nOpção inválida ! Por favor, escolha uma opção válida entre 1 e 4.\n")
    