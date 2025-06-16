menu = """
[d] Depósito
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("==========DEPÓSTIO==========")
        valor = float(input("Digite o valor do Depósito: "))

        if valor > 0:
            saldo += valor
        else:
            print("Valores negativos não podem ser depositados")
            break

        print(f"Depósito de R$:{valor: .2f}")



    elif opcao == "s":
        print("==========SAQUE==========")
        retirada = float(input("Digite o valor a ser retirado: "))
        if retirada > 500:
            print("Valor não pode ser sacado")

        elif retirada < 0:
            print("Valores negativos não podem ser sacados")

        elif retirada > saldo:
            print("Não a saldo Suficiente!")

        else:
            saldo -= retirada
            print("Saque realizado com Sucesso")




    elif opcao == "e":
        print("==========EXTRATO==========")
        print(f"Extrato R${saldo: .2f}")

    elif opcao == "q":
        break

    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")