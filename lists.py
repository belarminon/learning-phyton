frutas = ["laranja", "maca", "uva"]
print(frutas)

frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

print([n**2 if n > 6 else n for n in range(10) if n % 2 == 0])

# Sort

languages = ["python", "js", "c","java","csharp"]

print(sorted(languages, key=lambda x: len(x)))
print(sorted(languages, key=lambda x: len(x), reverse=True))