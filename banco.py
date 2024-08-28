menu = """

[d]
[s]
[e]
[q]

=> """


saldo = 0
limite = 1500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 5

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou, o valor informado é invalido.")

    elif opcao == "s":
        valor = float(input("informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("operação falhou! você nao tem saldo suficiente")

        elif excedeu_limite:
            print("operação falhou! o valor do saque excede o limite")

        elif excedeu_saques:
            print("operação falhou! você oxcedeu o numero de saques")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! o valor informado é invalido.")

    elif opcao == "e":
        print("\n=$=$=$=$=$=$=$=$= EXTRATO BANCÁRIO =#=#=#=#=#=#=")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("____________________________")
    elif opcao == "q":
        break
    else:
        print("operação invalida, por favor selecione novamente a operação desejada.")
