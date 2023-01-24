a_list = []
for i in range(6):
    a, b = input().split()
    a = int(a)
    b = int(b)
    c=(a,b)
    if c not in a_list:
        a_list.append(c)

print(a_list)