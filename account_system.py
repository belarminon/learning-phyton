
saldo = 0.00
limite = 500
numero_saque = 0
LIMITE_MAX_SAQUE = 3
changes = []

def add_change(description):
    changes.append(description)

def get_changes():
    return changes    

def withdraw(valor, saldo):
    if saldo >= valor:
        saldo -= saque
        add_change(f"Saque: {saque:.2f} Saldo: {saldo:.2f}")
        print(f'''
            Saque de R$ {valor:.2f} realizado com sucesso.
            Saldo atual: R$ {saldo:.2f}.
        ''')
        return saldo
    else: 
        print("Não será possivel sacar o dinheiro por falta de saldo. Saldo atual R$ {saldo:.2f}.")
        return saldo

def deposit(valor = 0):
    if valor > 0:
        valor += valor
        print(f'''
            Valor depositado: R$ {valor:.2f}.
            O teu saldo é de R${valor:.2f}.
        ''') 
        return valor
    else:
        print(f"O valor R$ {valor:.2f} não é válido. Deposite um valor válido.")

def account_statement():
    if saldo > 0:
        extract = " Extrato Geral da Conta Corrente "
        print(extract.center(100,"#"))
        for extract in get_changes():
            print(extract)
        print(f"O saldo atual é: R$ {saldo:.2f}.")
    else:
        print("Conta Corrente sem saldo.")

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
        saldo = deposit(deposito)
        add_change(f"Deposito: {deposito:.2f} Saldo: {saldo:.2f}")
        
   elif opcao == 2:
        if saldo > 0:
            if numero_saque <= LIMITE_MAX_SAQUE:

                print("Voce entrou na opção de Saque.")  
                saque = float(input("Qual valor deseja sacar: R$ "))

                if limite >= saque or LIMITE_MAX_SAQUE is not numero_saque:

                    numero_saque += 1
                    saldo = withdraw(saque, saldo)

                    numero_saque_restante = LIMITE_MAX_SAQUE - numero_saque
                    if numero_saque_restante != 0:
                        print(f"O limite restante de saque é: {numero_saque_restante}.")
                        # add_change(f"Saque: {saque:.2f} Saldo: {saldo:.2f}")
                    else:
                        print(f'''"
                            O limite máximo diário de {LIMITE_MAX_SAQUE} saques foi atingido.
                            Tente novamente amanhã.
                        ''')

                else:
                    print(f"Não é permitido sacar valor maior que R$ {limite:.2f}.")

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