import os
import platform
from datetime import date

# Classes para representar os clientes, contas e transações
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, descricao):
        self.transacoes.append(descricao)

class Transacao:
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.saldo += self.valor
        conta.historico.adicionar_transacao(f"Depósito de R$ {self.valor:.2f}")

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.saldo >= self.valor:
            conta.saldo -= self.valor
            conta.historico.adicionar_transacao(f"Saque de R$ {self.valor:.2f}")
            return True
        else:
            print("Saldo insuficiente!")
            return False

class Conta:
    def __init__(self, numero, agencia, cliente):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def saldo_atual(self):
        return self.saldo

    def sacar(self, valor):
        saque = Saque(valor)
        return saque.registrar(self)

    def depositar(self, valor):
        deposito = Deposito(valor)
        deposito.registrar(self)

class ContaCorrente(Conta):
    def __init__(self, numero, agencia, cliente, limite=500, limite_saques=3):
        super().__init__(numero, agencia, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_realizados = 0

    def sacar(self, valor):
        if self.saques_realizados < self.limite_saques:
            if valor <= self.limite:
                sucesso = super().sacar(valor)
                if sucesso:
                    self.saques_realizados += 1
                return sucesso
            else:
                print("O valor do saque excede o limite.")
        else:
            print("Número de saques diários excedido.")

# Funções de interface com o usuário e menu
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

def depositar(conta, valor):
    limpar_tela()
    if valor > 0:
        conta.depositar(valor)
        print("\nDepósito realizado!")
    else:
        print("\nFalha! Valor inserido inválido.")

def sacar(conta, valor):
    limpar_tela()
    if valor > 0:
        conta.sacar(valor)
    else:
        print("\nFalha! Valor inserido inválido.")

def exibir_extrato(conta):
    limpar_tela()
    print("\n############### EXTRATO ###############\n")
    if not conta.historico.transacoes:
        print("Não foram realizadas movimentações.\n")
    else:
        for transacao in conta.historico.transacoes:
            print(transacao)
    print(f"Saldo atual:\t\t  R$ {conta.saldo_atual():.2f}")
    print("#" * 40)

def criar_usuario(usuarios):
    limpar_tela()
    cpf = input("Informe o CPF (somente número): ")
    usuario = verifica_usuario(cpf, usuarios)
    if usuario:
        print("\nFalha! Já existe usuário cadastrado com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    logradouro = input("Logradouro: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    sigla_estado = input("Sigla estado: ")
    endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{sigla_estado}"
    usuario = PessoaFisica(cpf, nome, data_nascimento, endereco)
    usuarios.append(usuario)
    print("\nUsuário criado com sucesso!")

def verifica_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return usuario
    return None

def criar_conta(agencia, numero_conta, usuarios, contas):
    limpar_tela()
    cpf = input("Informe o CPF do usuário: ")
    usuario = verifica_usuario(cpf, usuarios)
    if usuario:
        conta = ContaCorrente(numero=numero_conta, agencia=agencia, cliente=usuario)
        usuario.adicionar_conta(conta)
        contas.append(conta)
        print("\nConta criada!")
    else:
        print("\nUsuário não encontrado! Tente novamente.")

def listar_contas(contas):
    limpar_tela()
    if not contas:
        print("Nenhuma conta foi encontrada.")
        return

    for conta in contas:
        linha = f"""
        Agência: {conta.agencia}
        C/C: {conta.numero}
        Titular: {conta.cliente.nome}
        """
        print("=" * 50)
        print(linha)

def listar_usuarios(usuarios):
    limpar_tela()
    if not usuarios:
        print("Nenhum usuário foi encontrado.")
        return

    for usuario in usuarios:
        linha = f"""\nNome: {usuario.nome}
        CPF: {usuario.cpf}
        Data de Nascimento: {usuario.data_nascimento}
        Endereço: {usuario.endereco}
        """
        print("=" * 50)
        print(linha)

def limpar_tela():
    sistema_operacional = platform.system()
    if sistema_operacional == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        limpar_tela()
        
        if opcao == "d":
            numero_conta = int(input("\nInforme o número da conta para depósito: "))
            conta = contas[numero_conta - 1]
            valor = float(input("Informe o valor para depósito: "))
            depositar(conta, valor)

        elif opcao == "s":
            numero_conta = int(input("\nInforme o número da conta para saque: "))
            conta = contas[numero_conta - 1]
            valor = float(input("Informe o valor para saque: "))
            sacar(conta, valor)

        elif opcao == "e":
            numero_conta = int(input("\nInforme o número da conta para extrato: "))
            conta = contas[numero_conta - 1]
            exibir_extrato(conta)

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            numero_conta = len(contas) + 1
            criar_conta(AGENCIA, numero_conta, usuarios, contas)

        elif opcao == "lc":
            listar_contas(contas)
        
        elif opcao == "lu":
            listar_usuarios(usuarios)

        elif opcao == "q":
            break

        else:
            print("\nOperação selecionada inválida! Por favor, tente novamente.")

# Executa a função principal
main()
