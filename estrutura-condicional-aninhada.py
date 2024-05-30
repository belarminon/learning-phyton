conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("saque realizado com sucesso!")
    elif saque <= (saldo - cheque_especial):
        print("saque realizado com o uso do cheque especial!")
    else:
        print("não foi possivel realizar o saque, saldo insuficiente")
elif conta_universitaria:
    if saldo >= saque:
        print("saque realizado com sucesso!")
    else:
        print("saldo insuficiente!")
else:
    print("didtema nao reconheceu seu tipo de conta, entre em contato com o teu gerente.")