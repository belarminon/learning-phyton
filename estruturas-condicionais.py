MAIOR_IDADE = 18

idade = int(input("Informe a tua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode consumir bebida alcoolica.")

if idade < MAIOR_IDADE:
    print("Ixi, é menor de idade.")