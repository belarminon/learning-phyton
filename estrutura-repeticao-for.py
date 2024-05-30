
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# Exemple using an interable

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()
    print("Executa no final do laço")

# Exemple using a buildt-in function RANGE

for number in range(0,11):
    print(number, end=" ")
    print()

for number in range(0, 51, 5):
    print(number, end=" ")