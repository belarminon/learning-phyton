def sacar(valor):
    saldo = 200

    if saldo >= valor:
        print("valor sacado: " + str(valor))
    else:
        print("valor insuficiente.")

sacar(300)