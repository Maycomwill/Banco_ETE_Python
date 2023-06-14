from os import system, name
from time import sleep

testeLogico = True
autenticado = False
depositoInicial = 0
ag = 0
account = 0
saldoCc = 0.0
saldoCp = 0.0
transacao = 0.0
nomeUsuario = ""


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


while testeLogico:

    print("---------------------------------")
    print("|\t   Bem vindo ao Banco ETE\t|")
    print("|Escolha uma opção:\t\t\t\t|")
    print("|1: Criar uma conta\t\t\t\t|")
    print("|2: Mostrar saldo\t\t\t\t|")
    print("|3: Depositar na Conta corrente\t|")
    print("|4: Sacar na Conta corrente\t\t|")
    print("|5: Aplicar na Conta poupança\t|")
    print("|6: Resgatar da Conta poupança\t|")
    print("|7: Exibir contas\t\t\t\t|")
    print("|0: Para sair\t\t\t\t\t|")
    print("---------------------------------\n")
    menu = int(input("Escolha uma opção do menu: "))

    if menu == 1:

        if nomeUsuario == "":
            nomeDoUsuario = input("Digite seu nome: ")
            ag = int(input("Digite o número de sua agência: "))
            account = int(input("Digite o número da sua conta: "))

            print("\nBem vindo ao Banco ETE: ", nomeDoUsuario, "")
            print("Sua agência é:", ag)
            print("Sua conta corrente é a: {}-0".format(account))
            print("Sua conta poupança é a: {}-1".format(account))

            autenticado = True

            depositoInicial = int(input("\nVocê deseja fazer um depósito inicial? 1: Sim, 2: Não: "))

            if depositoInicial == 1:
                saldoCc = int(input("Digite o valor do depósito: R$ "))
                print("Seu saldo atual é:", "\nConta corrente: R${}\tConta poupança: R${}".format(saldoCc, saldoCp))
                sleep(2)
            else:
                print("Tudo bem, escolha uma opção de nosso menu \n")
        else:
            print("Você já possui uma conta, é permitdo apenas um usuário por exercução")
            sleep(2)

    elif menu == 2:
        if autenticado:
            print("Seu saldo atual na Conta corrente é: R${}".format(saldoCc))
            print("Seu saldo atual na Conta poupança é: R${}".format(saldoCp))
            sleep(2)
        else:
            print("Desculpe, você precisa criar uma conta, antes de realizar qualquer operação!\n")
    elif menu == 3:
        if autenticado:
            transacao = float(input("Digite o valor de depósito: R$"))
            saldoCc += transacao
            transacao = 0.0

            print("Operação realizada com sucesso\n")
            print("Seu novo saldo é: R${}".format(saldoCc))
            sleep(2)
        else:
            print("Desculpe, você precisa criar uma conta, antes de realizar qualquer operação!\n")

    elif menu == 4:
        if autenticado:
            transacao = float(input("Digite o valor que você deseja sacar: R$"))

            if transacao > saldoCc:
                print("Você não possui saldo suficiente para o saque!\n")

            else:
                saldoCc -= transacao
                transacao = 0.0
                print("Operação realizada com sucesso\n")
                print("Seu novo saldo é de: R${}".format(saldoCc))
                sleep(2)
        else:
            print("Desculpe, você precisa criar uma conta, antes de realizar qualquer operação!\n")

    elif menu == 5:
        if autenticado:
            transacao = float(input("Digite o valor que você deseja transferir para a conta poupança: R$"))

            if transacao > saldoCc:
                print("Você não possui saldo suficiente para a transferência!\n")
            else:
                saldoCc -= transacao
                saldoCp += transacao
                transacao = 0.0
                print("Operação realizada com sucesso\n")
                print("Seu novo saldo na Conta corrente é de: R${}".format(saldoCc))
                print("Seu novo saldo na Conta poupança é de: R${}".format(saldoCp))
                sleep(2)
        else:
            print("Desculpe, você precisa criar uma conta, antes de realizar qualquer operação!\n")

    elif menu == 6:
        if autenticado:
            transacao = float(input("Digite o valor que você deseja resgatar da conta poupança: R$"))

            if transacao > saldoCp:
                print("Você não possui saldo suficiente para resgatar!\n")
            else:
                saldoCp -= transacao
                saldoCc += transacao
                transacao = 0.0
                print("Operação realizada com sucesso\n")
                print("Seu novo saldo na Conta corrente é de: R${}".format(saldoCc))
                print("Seu novo saldo na Conta poupança é de: R${}".format(saldoCp))
                sleep(2)
        else:
            print("Desculpe, você precisa criar uma conta, antes de realizar qualquer operação!\n")

    elif menu == 7:
        if autenticado:
            print("\nSuas contas são:\n")
            print("Conta corrente: {}-0".format(account))
            print("Conta poupança: {}-1".format(account))
            sleep(2)
        else:
            print("Desculpe, você precisa criar uma conta, antes de realizar qualquer operação!\n")

    elif menu == 0:
        print("Obrigado por usar o Banco ETE, volte sempre!\n\n")
        autenticado = False
        testeLogico = False
    else:
        print("\nOpção inválida, por favor, selecione um opção apresentada no menu\n")
