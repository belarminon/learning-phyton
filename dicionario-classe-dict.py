# Iteration into dictionary
contacts = {
    "belarnicolau@hotmail.com":{"name":"Belarmino", "phone": "(12) 98845-0080"},
    "belarnicolau@gmail.com":{"name":"Belarmino", "phone": "(12) 98845-0080"},
    "belarmino.nicolau@bnms.com.br":{"name":"Belarmino", "phone": "(12) 93333-3333"},
    "belarmino.nicolau@fsservices.com.br":{"name":"Belarmino", "phone": "(12) 98845-0080"},
    "belarmino.simao@uaga.com.br":{"name":"Belarmino", "phone": "(12) 98845-0080"},
    "belarmino.simao@meta.com.br":{"name":"Belarmino", "phone": "(12) 98845-0080"},
    "belarmino.simao@decision.com.br":{"name":"Belarmino", "phone": "(12) 97777-7777"},
    "belarmino.simao@onset.com.br":{"name":"Belarmino", "phone": "(12) 98845-0080"},
    "belarminon@compnet.com.br":{"name":"Belarmino", "phone": "(12) 99999-9999"},
}

# method clear()
# print(contacts.clear())

# method copy()
copy = contacts.copy()
copy["belarmino.nicolau@bnms.com.br"] = dict(name="BNMS", phone="(22) 91111-1111")
print(copy)

# method dict.fromkeys
print(dict.fromkeys(["name","phone"])) # with empty key
print(dict.fromkeys(["name","phone"], "Empty")) # with default value ("empty")

# method get => to access value from dictionary
# print(contacts["key"]) # KeyError
print(contacts.get("key")) # None
print(contacts.get("key", {})) # {} empty dictionary when key does not exist
print(copy.get("belarmino.nicolau@bnms.com.br", {})) # {'name': 'BNMS', 'phone': '(22) 91111-1111'}

# method items()
print(copy.items()) # return a list of tuples and usefull to interation with for command

# method keys()
print(copy.keys()) # return only the dictionary keys

# method pop() => remove
print(copy.pop("belarmino.nicolau@bnms.com.br")) # {'name': 'BNMS', 'phone': '(22) 91111-1111'}
print(copy.pop("belarmino.nicolau@bnms.com.br", {})) # {}

# method popitem()
# copy.popitem() # KeyError: 'popitem(): dictionary is empty'

# method setdefault()
copy.setdefault("age", 55)
print(copy)

# method update()
contacts.update({"belarminon@compnet.com.br":{"name":"Belarmino CompNet", "phone": "(22) 92222-2222"}})
print(contacts)

contacts.update({"belarminon@facebook.com":{"name":"Belarmino Facebook", "phone": "(22) 93333-3333"}})
print(contacts)

# method values()
print(contacts.values()) # return only the dictionary values

# method in()
print("belarminon@facebook.com" in contacts)
print("miguxa@xaxa.mim.br" in contacts)
print("age" in contacts["belarminon@facebook.com"])
print("phone" in copy["belarmino.simao@meta.com.br"])

# method del()
del contacts["belarmino.nicolau@fsservices.com.br"]["phone"]
print(contacts)
del contacts["belarmino.simao@uaga.com.br"]
print(contacts)