n1 = int(input())
value = {}
for i in range(n1):
    name, price = input().split()
    value[name] = float(price) 

total = 0
seller = {}
n2 = int(input())
for j in range(n2):
    product, j = input().split()
    if product in value: 
        p = value[product] * int(j)
        if product in seller:
            seller[product] += p
        else:
            seller[product] =  p
        total += p
        
if total == 0: 
    print("No ice cream sales")
else:
    x = [[seller[ice],ice] for ice in seller] 
    maxvalue = max(x)[0] 
    mv = [x for s,x in x if s == maxvalue]
    mv.sort() 
    print("Total ice cream sales:", total)
    print('Top sales:',' ,'.join(mv))