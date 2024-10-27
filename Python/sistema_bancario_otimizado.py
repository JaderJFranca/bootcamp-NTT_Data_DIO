import os
import platform

# Função que exibe o menu e solicita a opção desejada do usuário
def menu():
    menu = """
    ============== MENU ==============
    [d] \tDepositar
    [s] \tSacar
    [e] \tExtrato
    [u] \tCriar Usuário
    [c] \tCriar Conta
    [lc] \tListar Contas
    [lu] \tListar Usuários
    [q] \tSair

    Digite a opção desejada: """
    return input(menu)

# Função para realizar o depósito
def depositar(saldo, valor, extrato, /):
    limpar_tela()  # Limpa a tela antes de realizar a operação

    # Verifica se o valor de depósito é positivo
    if valor > 0:
        saldo += valor  # Adiciona o valor ao saldo
        extrato += f"\nDepósito:\t\t+ R$ {valor:.2f}\n"  # Registra o depósito no extrato
        print("\nDepósito realizado!")
    else:
        print("\nFalha! Valor inserido inválido.")
    
    return saldo, extrato

# Função para realizar o saque
def sacar(*, valor, saldo, extrato, limite, limite_saques, saques):
    limpar_tela()  # Limpa a tela antes de realizar a operação

    # Verifica se o saldo é suficiente para o saque
    if valor > saldo:
        print("\nFalha! Você não tem saldo suficiente.")
    # Verifica se o valor do saque é maior que o limite permitido
    elif valor > limite:
        print("\nFalha! O valor de saque excedeu o limite.")
    # Verifica se o número máximo de saques diários foi atingido
    elif saques >= limite_saques:
            print("\nFalha! Número de saques diários excedido.")
    # Verifica se o valor do saque é válido (positivo)
    elif valor > 0:
        saldo -= valor  # Subtrai o valor do saldo
        extrato += f"\nSaque:\t\t\t- R$ {valor: .2f}\n"  # Registra o saque no extrato
        print("\nSaque realizado!")
        saques += 1  # Incrementa o número de saques realizados
    else:
        print("\nFalha! Valor inserido inválido.")

    return saldo, extrato, saques

# Função para exibir o extrato
def exibir_extrato(saldo, /, *, extrato):
    limpar_tela()  # Limpa a tela antes de exibir o extrato

    print("\n############### EXTRATO ###############\n")
    # Exibe o extrato ou informa que não houve movimentações
    print("Não foram realizadas movimentações.\n" if not extrato else extrato)
    print(f"Saldo atual:\t\t  R$ {saldo:.2f}")
    print("#" * 40)

# Função para criar um novo usuário
def criar_usuario(usuarios):
    limpar_tela()  # Limpa a tela antes do cadastro

    # Solicita o CPF e verifica se já existe um usuário com o mesmo CPF
    cpf = input("Informe o CPF (somente número): ")
    usuario = verifica_usuario(cpf, usuarios)

    if usuario:
        print("\nFalha! Já existe usuário cadastrado com esse CPF!")
        return

    # Coleta os dados do novo usuário
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    logradouro = input("Logradouro: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    sigla_estado = input("Sigla estado: ")

    # Monta o endereço formatado
    endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{sigla_estado}"

    # Adiciona o novo usuário à lista de usuários
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("\nUsuário criado com sucesso!")

# Função para verificar se o usuário já existe com base no CPF
def verifica_usuario(cpf, usuarios):
    # Filtra os usuários pela lista com base no CPF
    filtro_usuarios = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return filtro_usuarios[0] if filtro_usuarios else None

# Função para criar uma nova conta associada a um usuário
def criar_conta(agencia, numero_conta, usuarios):
    limpar_tela()  # Limpa a tela antes do cadastro

    # Solicita o CPF e verifica se o usuário está cadastrado
    cpf = input("Informe o CPF do usuário: ")
    usuario = verifica_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado! Tente novamente.")

# Função para listar as contas cadastradas
def listar_contas(contas):
    limpar_tela()  # Limpa a tela antes de exibir as contas

    if not contas:  # Verifica se há contas cadastradas
        print("Nenhuma conta foi encontrada.")
        return

    # Exibe os dados de cada conta
    for conta in contas:
        linha = f"""
        \nAgência: {conta['agencia']}
        \nC/C: {conta['numero_conta']}
        \nTitular: {conta['usuario']['nome']}
        """
        print("=" * 50)
        print(linha)

# Função para listar os usuários cadastrados
def listar_usuarios(usuarios):
    limpar_tela()  # Limpa a tela antes de exibir os usuários

    if not usuarios:  # Verifica se há usuários cadastrados
        print("Nenhum usuário foi encontrado.")
        return

    # Exibe os dados de cada usuário
    for usuario in usuarios:
        linha = f"""\nNome: {usuario['nome']}
        \nCPF: {usuario['cpf']}
        \nData de Nascimento: {usuario['data_nascimento']}
        \nEndereço: {usuario['endereco']}
        """
        
        print("=" * 50)
        print(linha)

# Função para limpar a tela, de acordo com o sistema operacional
def limpar_tela():
    sistema_operacional = platform.system()
    
    # Limpa a tela no Windows
    if sistema_operacional == "Windows":
        os.system("cls")
    # Limpa a tela no Linux ou macOS
    else:
        os.system("clear")

# Função principal que controla o fluxo do programa
def main():

    # Definindo variáveis globais
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    saques = 0
    usuarios = []
    contas = []
    

    # Loop principal que mantém o programa em execução
    while True:
        
        opcao = menu()  # Exibe o menu e solicita uma opção
        limpar_tela()
        
        # Opções para cada funcionalidade do menu
        if opcao == "d":
            valor = float(input("\nInforme o valor para depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("\nInforme o valor para saque: "))
            saldo, extrato, saques = sacar(
                valor=valor,
                saldo=saldo,
                extrato=extrato,
                limite=limite,
                limite_saques=LIMITE_SAQUES,
                saques=saques,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            numero_conta = len(contas) + 1  # Define o número da conta com base na quantidade de contas
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)
        
        elif opcao == "lu":
            listar_usuarios(usuarios)

        elif opcao == "q":
            break  # Encerra o programa

        else:
            print("\nOperação selecionada inválida! Por favor, tente novamente.")

# Executa a função principal
main()
