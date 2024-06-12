# Iteration into dictionary
contacts = {
    "belarnicolau@hotmail.com":{"name":"Belarmino", "phone": "(12) 98845-0080"},
    "belarnicolau@gmail.com":{"name":"Belarmino", "phone": "(12) 98845-0080"},
    "belarmino.nicolau@bnms.com.br":{"name":"Belarmino", "phone": "(12) 98845-0080"},
    "belarmino.nicolau@fsservices.com.br":{"name":"Belarmino", "phone": "(12) 98845-0080"},
    "belarmino.simao@uaga.com.br":{"name":"Belarmino", "phone": "(12) 98845-0080"},
    "belarmino.simao@meta.com.br":{"name":"Belarmino", "phone": "(12) 98845-0080"},
    "belarmino.simao@decision.com.br":{"name":"Belarmino", "phone": "(12) 96666-6666"},
    "belarmino.simao@onset.com.br":{"name":"Belarmino", "phone": "(12) 98845-0080"},
    "belarminon@compnet.com.br":{"name":"Belarmino", "phone": "(12) 98845-0080"},
}

print(contacts["belarmino.simao@decision.com.br"]["phone"])

for key in contacts:
    print(key, contacts[key])

for key, value in contacts.items():
    print(key, value)