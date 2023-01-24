Number_Input1 = int(input())
value = {}
for i in range(Number_Input1):
    ice_cream , val = input().split()
    value[ice_cream] = int(val)

total = 0
seller = {}
Number_Input2 = int(input())
for j in range(Number_Input2):
    product , j = input().split()
    if product in value:
        val = value[product]*int(j)
        if product in seller:
            seller[product] += val
        else:
            seller[product] = val
        total += val
if total == 0:
    print("No ice cream sales")
else:
    x = []
    for ice_cream in seller:
        x.append(seller[ice_cream], ice_cream)
    max_seller = max(x)[0]
    y = []
    for z, ice_cream in x:
        if z == max_seller:
            y.append(ice_cream)
    y.sort()
    print("Total Ice cream sales:", total)
    print("Top sales:",' ,'.join(y))