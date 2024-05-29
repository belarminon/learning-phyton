product_1 = 2
product_2 = 3

print(product_1 + product_2) # add
print(product_1 - product_2) # substract
print(product_1 / product_2) # divide - return a number with decimal point
print(product_1 // product_2) # return only number after the decimal point
print(product_1 * product_2) # multiply
print(product_1 ** product_2) # exponent
print(product_1 % product_2) # modulo - return only int part

# precedence

x= 4 + 5 * 6
print(x)
x= (4 + 5) * 6
print(x)
x= 4 + (5 * 6)
print(x)