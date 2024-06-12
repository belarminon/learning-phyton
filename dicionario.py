# Umio dicionario é um conjunto não-ordernado de pares chave:valor, onde as chaves são unicas em uma dada instancia do dicionário. Dicionário são limitados por chaves: {}, e contém uma lista de pares chave:valor separada por vírgulas.

#define a values
person = {"name":"Belarmino", "age":43}
print(person)
person = dict(name="Belarmino", age=43)
print(person)

#add ney key "phone"
person["phone"] = "(12) 98845-0080"
print(person)