
saldo = 0.00
limite = 500
numero_saque = 0
LIMITE_MAX_SAQUE = 3
changes = []

def add_change(description):
    changes.append(description)

def get_changes():
    return changes    

def withdraw(valor, saldo, limite):

    if saldo >= valor: #don't permit negative valoues
            
        if limite >= valor: # don't permit valor bigger than 500.00
                
            saldo -= valor
            add_change(f"Saque: R$ {valor:.2f} Saldo: R$ {saldo:.2f}")
            print(f'''
                Saque de R$ {valor:.2f} realizado com sucesso.
                Saldo atual: R$ {saldo:.2f}.
            ''')

            return saldo

        else:
            print(f"Não é permitido sacar valor maior que R$ {limite:.2f}.")

    else: 
        print("Não será possivel sacar o dinheiro por falta de saldo. Saldo atual R$ {saldo:.2f}.")
        return saldo

def deposit(valor, saldo):
    if valor > 0:
        saldo += valor
        add_change(f"Deposito: R$ {valor:.2f} Saldo: R$ {saldo:.2f}")
        print(f'''
            Valor depositado: R$ {valor:.2f}.
            Saldo atual: R$ {saldo:.2f}.
        ''') 
        return saldo
    else:
        print(f"O valor R$ {valor:.2f} não é válido. Deposite um valor válido.")

def account_statement():
    print()
    extract = " Extrato Geral da Conta Corrente "
    print(extract.center(100,"#"))
    if saldo > 0:
        for extract in get_changes():
            print(extract)
        print(f"O saldo atual é: R$ {saldo:.2f}.")
    else:
        print("Conta Corrente sem saldo.")
    
    print(_.center(100,"#"))

menu = '''
    [1] - Depositar ( Deposit )
    [2] - Sacar ( Withdraw )
    [3] - Extrato ( Current Account Statement)
    [0] - Sair ( Exit )

    => '''

add_change(f"Saldo Inicial: R$ {saldo:.2f}")

while True:

   opcao = int(input(menu))

   if opcao == 1:
        print("Voce entrou na opção de Deposito") 
        deposito = float(input("Qual valor desejas deposit: "))
        saldo = deposit(deposito, saldo)
        
   elif opcao == 2:
        
        if saldo > 0:

            if numero_saque is not LIMITE_MAX_SAQUE:

                numero_saque += 1

                print("Voce entrou na opção de Saque.")  
                saque = float(input("Qual valor deseja sacar: R$ "))
                saldo = withdraw(saque, saldo, limite)

                print(f"O limite restante de saque é: {LIMITE_MAX_SAQUE - numero_saque}.")

            else:
                print(f"O limite de {LIMITE_MAX_SAQUE} saques diarios foi alcançado.")
                
        else:
            print("Não será possivel sacar o dinheiro por falta de saldo. Saldo atual R$ {saldo:.2f}.")
            
   elif opcao == 3:
        account_statement()

   elif opcao == 0:
        break

   else:
        print("Operação inválida. Por favor selecionar novamente a operação desejada.")