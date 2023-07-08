#Desafio criando um sistema bancario com python
menu  = """
[d] Depositar
[s] Sacar
[e] Extrato
[t] Transferir
[q] Sair
=> """
saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 4

while True:

    opcao = input(menu)

    if opcao == "d":
        valor= float(input("Informe o valor para o depósito"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("A operação falhou o valor informado é menor que 0. Por favor informe um valor maior que zero.")

    elif opcao == "s":
        valor= float(input("Informe o valor do saque"))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! Esse valor supera o limite de saque.")
        elif excedeu_saques:
            print("Operação falhou! Número de saques do dia foram excedidos. Por favor retorne amanhã")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n======================EXTRATO======================")
        print("\n Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n===================================================")
    
    elif opcao == "t":
        transferir = float(input("Informe o valor que deseja transferir"))
        if transferir > saldo :
            print("O valor informado supera o saldo disponível")
        elif transferir < saldo and transferir > 0:
            saldo -= transferir
            extrato += f"Trasferência: R$ {transferir:.2f}\n"
    
    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada")