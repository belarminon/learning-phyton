# Strings de multiplas linhas sao definidas informando 3 aspas simples ou duplas durantea atribuição. 
# Elas podem ocupar varias linhas do código e todos os espaços em branco sao incluidos na string final

name = "Belarmino"

message = f"""
  Hello my name is {name},
I'm found of phyton
"""

print(message)

message = f'''
    Hello my name is {name},
I'm found of        phyton
'''

print(message)