def depositar(saldo):
    dep = float(input("Digite o valor que deseja depositar: "))
    while dep < 0:
        print("NÃO SE PODE DIGITAR UM VALOR NEGATIVO!!!!")
        dep = float(input("Digite o valor que deseja depositar: "))
    saldo += dep
    print(f"Seu depósito de R${dep:.2f} foi realizado com sucesso!")
    return saldo

def sacar(saldo, numerosaque, LIMITE, extratosaque):
    if numerosaque >= LIMITE:
        print("SAQUE NEGADO VOCÊ PASSOU DO LIMITE DIARIO!")
        return saldo, numerosaque, LIMITE, extratosaque
    saque = float(input(f""" 
                        
                        SAQUES DIARIOS RESTANTES {LIMITE-numerosaque}
                        SALDO ATUAL: R$ {saldo:.2f}
                        Digite o valor que deseja sacar (até 500 reais)
                        
                        => """))
    
    while saque > 500 or saque < 0:
        print("DIGITE UM VALOR DE SAQUE VALIDO")
        saque = float(input(f""" SAQUES DIARIOS RESTANTES {LIMITE-numerosaque}
                        
                        SALDO ATUAL: R$ {saldo:.2f}
                        Digite o valor que deseja sacar (até 500 reais)
                        
                        => """))
    

    if saque > saldo:
        print("Você não tem esse valor cancelando operação...")
        return saldo, numerosaque, LIMITE, extratosaque

    saldo = saldo - saque
    numerosaque +=1
    extratosaque.append(saque)
    return saldo, numerosaque, LIMITE, extratosaque

def extratos(valor):
    return valor


menu = """
Digite a opção desejada:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """


saldo = 0
limite = 500
extratosaque = []
extratosaldo = []
numero_saques = 0
LIMITE_SAQUES = 3 

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        saldo = depositar(saldo)
        print(f"Seu valor de deposito é: {saldo}")
        extratosaldo.append(extratos(saldo))

    elif opcao == "s":
        print("Saque")
        saldo, numero_saques, LIMITE_SAQUES,extratosaque = sacar(saldo, numero_saques, LIMITE_SAQUES, extratosaque)
        print(f"SEU SALDO ATUAL É {saldo:.2f}, VOCÊ TEM {LIMITE_SAQUES-numero_saques} SAQUES RESTANTES")

    elif opcao == "e":
        print("Extrato")
        print(f"SALDO DA CONTA {saldo}")
        print(f"Você depositou dinheiro {len(extratosaldo)} vezes")
        for i, valor in enumerate(extratosaldo, start=1):
            print(f"{i}º Deposito R$ {valor:.2f}")

        print(f"Você depositou dinheiro {len(extratosaque)} vezes")
        for i, valor in enumerate(extratosaque, start=1):
            print(f"{i}º Saque R$ {valor:.2f}")

    elif opcao == "q":
        print("Saindo...")
        break
    
    else:
        print("Opção errada! Digite novamente!")