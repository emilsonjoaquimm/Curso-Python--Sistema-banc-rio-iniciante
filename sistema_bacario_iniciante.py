print('Bem vindo ao Banco do curso Python ')

menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3
msg = 'Por favor, digite um valor valido!!! '

while True:
# Opção de depósito:
    opcao = input(f'\n Digite uma opção: {menu}')
 
    if opcao == "d":
        valor = float(input('Informe o valor do depósito: '))

        if valor > 0:
            saldo +=valor
            extrato += (f'Depósito: R$ {valor:.2f}\n')

        else:
            print('O valor informado é inválido.')
# Opcao de saque:
    elif opcao == "s":
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor >saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Você não possui saldo suficiente. ")

        elif excedeu_limite:
            print('O valor do saque excede o seu limite da conta. ')

        elif excedeu_saques:
            print('Quantidades de saques diários excedidos. ')

        elif valor > 0:
            saldo -= valor
            extrato += (f' Saque: R$ {valor:. 2f} \n')
            numero_saques += 1

        else:
            print('A operação falhou! O valor informado é inválido.')

      # Extrato:
    elif opcao == "e":
        print(' \n ==========EXTRATO==========')
        print("Não foram realizadas movimentações. " if not extrato else extrato)
        print(f'\n Saldo: R$ {saldo:.2f}')
        print("===============================")
    
    # Opção de sair:
    elif opcao == "q":
        break

    else: 
        print(" Operação inválida, por favor selecione novamente a operação desejada.")


