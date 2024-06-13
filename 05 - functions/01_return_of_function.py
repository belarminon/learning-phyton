def amounts(number):
    return sum(number)

def return_first_and_last(number):
    first = number - 1
    last = number + 1

    return first, last

print(amounts([5, 15, 25])) # 45
print(return_first_and_last(10)) # (9, 11)