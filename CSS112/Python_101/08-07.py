def total(pocket):
    summation = 0
    for money in pocket:
        summation += money*pocket[money] 
    return summation

def take(pocket, money_in):
    for money in money_in:
        if money in pocket:
            pocket[money] += money_in[money]
        else:
            pocket[money] = money_in[money]
    return

def pay(pocket, amt):
    money_out = {}
    for money in sorted(pocket.key())[::-1]:
        if amt >= money:
            result = (pocket[money], amt//money)
            money_out[money] = result
            pocket[money] -= result
            amt -= money*result
    if amt > 0:
        take(pocket, money_out)
        money_out = {}
    return money_out

# exec(input().strip())