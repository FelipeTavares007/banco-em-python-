nome = 0
dinheiro = 1500
senha = 1209


def interacoes():
    global dinheiro

    while True:
        print("\nSeja bem vindo ao banco Feltav \n")
        print(" 1 - Depositar dinheiro")
        print(" 2 - Sacar dinheiro")
        print(" 3 - Ver saldo")
        print(" 4 - Sair \n")
        opcao = input("Selecione uma opção: ")

        match opcao:
            case "1":
                dinheiro = depositar(dinheiro)
            case "2":
                dinheiro = sacar(dinheiro)
            case "3":
                ver_saldo(dinheiro)
            case "4":
                print("Obrigado por usar o banco Feltav!")
                break
            case _:
                print("Opção inválida, tente novamente.")




def depositar(saldo):
    deposito = float(input("Digite o valor que deseja depositar: "))
    saldo = deposito + saldo

    print("Dinheiro depositado com sucesso")

    return saldo


def sacar(saldo):
    sacard = float(input("Digite o valor que deseja sacar: "))
    saldo = sacard - saldo

    print("Dinheiro sacado com sucesso")

    return saldo

def ver_saldo(saldo):
    print(f"Seu saldo atual é {saldo}")

    return saldo


nome = input("Olá! Digite seu nome: ")


for tentativa in range(3):
    senha = int(input("Digite a senha: "))
    if senha == 1209:
        print("Senha correta!")
        break
    else:
        print("Senha incorreta, tente novamente")
else:
    print("Número máximo de tentativas atingido.")


interacoes()








