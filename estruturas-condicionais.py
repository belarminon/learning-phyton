MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe a tua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode consumir bebida alcoolica.")
elif idade == IDADE_ESPECIAL:
    print("Pode segurar a latinha de cerveja rsrsr.")
else:
    print("Ixi, é menor de idade.")