def add(a, b):
    return a + b

def devi(a, b):
    return a / b

def multi(a, b):
    return a * b

def subst(a, b):
    return a - b

def display_result(a, b, operator):
    operation = ""
    if operator == add:
        operation = "+"
        result = operator(a, b)
    elif operator == subst:
        operation = "-"
        result = operator(a, b)
    elif operator == devi:
        operation = "/"
        result = operator(a, b)
    elif operator == multi:
        operation = "*"
        result = operator(a, b)

    print(f"The result of this operation {a} {operation} {b} = {result}")

display_result(5, 11, multi)