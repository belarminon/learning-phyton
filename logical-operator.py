
# AND
print(True and True)
print(True and False)
print(False and False)

# OR 
print(True or True)
print(True or False)
print(False or False)

balance = 1000
server = 250
limit = 200
conta_especial = True

exp = balance >= server and server <= limit or conta_especial and balance >= server
print('First expression ' + str(exp))
exp = (balance >= server and server <= limit) or (conta_especial and balance >= server)
print('Second expression ' + str(exp))

normal_account_with_balance = (balance >= server and server <= limit)
special_account_with_balance = (conta_especial and balance >= server)

result = normal_account_with_balance or special_account_with_balance
print(result)