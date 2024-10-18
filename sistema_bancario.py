import os

menu = '''
#### MENU ####
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Digite a opção desejada: '''
saldo = 0
limite = 500
extrato = ""
saques_diarios = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    os.system("cls")
    if opcao == "d":
        valor = float(input("\nInforme o valor para depósito: "))
        os.system("cls")
        if valor > 0:
            saldo += valor
            extrato = saldo
            print(f"\nSeu depósito foi: R$ {valor:.2f}\n")
        else:
            print("\nFalha! Valor inserido inválido.")

    elif opcao == "s":

        valor = float(input("\nInforme o valor para saque: "))
        os.system("cls")
        if valor > saldo:
            print("\nFalha! Você não tem saldo suficiente.")

        elif valor > limite:
            print("\nFalha! O valor de saque excedeu o limite.")
        
        elif saques_diarios >= LIMITE_SAQUES:
            print("\nFalha! Número de saques diários excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato = saldo
            saques_diarios += 1
        
        else:
            print("\nFalha! Valor inserido inválido.")
    
    elif opcao == "e":
        os.system("cls")
        print("\n############# EXTRATO #############\n")
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(f"Saldo atual: {saldo:.2f}")
        print("\n###################################")

    elif opcao == "q":
        break

    else:
        print("\nOperação selecionada inválida! Por favor, tente novamente.")