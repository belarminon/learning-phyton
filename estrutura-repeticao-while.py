opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("sacado...")
    elif opcao == 2:
        print("Exibindo o extrato...")
    elif opcao == 0:
        # sys.exit
        print("implementar a function para sair")
    else:
        print("Opção inválida")

# while with break and continue

while True:

    number = int(input("number: "))

    if number == 10:
        break

    if number % 2 == 0:
        continue

    print(number)