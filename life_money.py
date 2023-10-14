from itertools import accumulate

def life_money_calc(age, money_bag):
    total = 0
    for i in money_bag:
        total += i
        print(total)
        
    return total*age
