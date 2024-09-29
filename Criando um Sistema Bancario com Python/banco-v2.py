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
        print("DIGITE UM VALOR DE SAQUE VÁLIDO")
        saque = float(input(f""" SAQUES DIARIOS RESTANTES {LIMITE-numerosaque}
                       
                        SALDO ATUAL: R$ {saldo:.2f}
                        Digite o valor que deseja sacar (até 500 reais)
                       
                        => """))

    if saque > saldo:
        print("Você não tem esse valor, cancelando operação...")
        return saldo, numerosaque, LIMITE, extratosaque

    saldo -= saque
    numerosaque += 1
    extratosaque.append(saque)
    return saldo, numerosaque, LIMITE, extratosaque

def extratos(valor):
    return valor

def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    cpf = input("Digite o CPF (apenas números): ")
    
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Este CPF já está cadastrado!")
            return

    endereco = input("Digite o endereço (logradouro - número - bairro - cidade/sigla estado): ")

    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(usuario)
    print(f"Usuário {nome} criado com sucesso!")

def criar_conta():
    global conta_sequencial
    cpf = input("Digite o CPF do usuário para vincular a conta: ")

    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        print("Usuário não encontrado! Crie um usuário antes de criar uma conta.")
        return

    conta = {
        "agencia": "0001",
        "numero_conta": conta_sequencial,
        "usuario": usuario_encontrado,
        "saldo": 0,
        "extratosaque": [],
        "numero_saques": 0
    }
    contas.append(conta)
    conta_sequencial += 1
    print(f"Conta número {conta['numero_conta']} criada com sucesso para {usuario_encontrado['nome']}!")

def encontrar_conta_por_cpf(cpf):
    for conta in contas:
        if conta["usuario"]["cpf"] == cpf:
            return conta
    return None

menu = """
Digite a opção desejada:

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuário
[c] Criar Conta Corrente
[q] Sair

=> """

usuarios = []
contas = []
conta_sequencial = 1
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        cpf = input("Digite o CPF para fazer o depósito: ")
        conta = encontrar_conta_por_cpf(cpf)
        if conta:
            conta["saldo"] = depositar(conta["saldo"])
        else:
            print("Conta não encontrada. Crie uma conta primeiro.")

    elif opcao == "s":
        cpf = input("Digite o CPF para fazer o saque: ")
        conta = encontrar_conta_por_cpf(cpf)
        if conta:
            conta["saldo"], conta["numero_saques"], LIMITE_SAQUES, conta["extratosaque"] = sacar(
                conta["saldo"], conta["numero_saques"], LIMITE_SAQUES, conta["extratosaque"]
            )
        else:
            print("Conta não encontrada. Crie uma conta primeiro.")

    elif opcao == "e":
        cpf = input("Digite o CPF para ver o extrato: ")
        conta = encontrar_conta_por_cpf(cpf)
        if conta:
            print(f"SALDO DA CONTA: R$ {conta['saldo']:.2f}")
            print(f"Você realizou {len(conta['extratosaque'])} saques:")
            for i, valor in enumerate(conta['extratosaque'], start=1):
                print(f"{i}º Saque: R$ {valor:.2f}")
        else:
            print("Conta não encontrada. Crie uma conta primeiro.")

    elif opcao == "u":
        criar_usuario()

    elif opcao == "c":
        criar_conta()

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Opção inválida! Tente novamente.")
