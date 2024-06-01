# criar um sistema bancario com as operacoes: sacar, deositar e visualizar extrato
def sacar(valor):
    saldo = 200

    if saldo >= valor:
        print("valor sacado: " + str(valor))
    else:
        print("valor insuficiente.")

menu = '''
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [0] - Sair

    => 
'''


saldo = 0
limite = 500
numero_saque = 0
LIMITE_MAX_SAQUE = 3

print(menu)

# while True:

#    opcao = int(input(menu))

#    if opcao == 1:
#         print("Deposito")
        
#    elif opcao == 2:
#         print("Saque")
#         # sacar(300)

#    elif opcao == 3:
#         print("Extrato")

#    elif opcao == 0:
#         break

#    else:
#         print("Operação inválida. Por favor selecionar novamente a operação desejada.")



# conta_normal = True
# conta_universitaria = False

# saldo = 2000
# saque = 2500
# cheque_especial = 450

# if conta_normal:
#     if saldo >= saque:
#         print("saque realizado com sucesso!")
#     elif saque <= (saldo - cheque_especial):
#         print("saque realizado com o uso do cheque especial!")
#     else:
#         print("não foi possivel realizar o saque, saldo insuficiente")
# elif conta_universitaria:
#     if saldo >= saque:
#         print("saque realizado com sucesso!")
#     else:
#         print("saldo insuficiente!")
# else:
#     print("didtema nao reconheceu seu tipo de conta, entre em contato com o teu gerente.")