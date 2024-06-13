bill = 2000

def bill_bonus(bonus, list):
    global bill

    aux_list = list.copy()
    aux_list.append(2)
    print(f"list aux = {aux_list}")

    bill += bonus
    return bill

list = [1]
print(bill_bonus(500, list), list )