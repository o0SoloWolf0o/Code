Number_Input1 = int(input())
name = {}
for i in range(Number_Input1):
    n1 , n2 = input().split()
    name[n1] = n2
    name[n2] = n1
Number_Input2 = int(input())
x = []
for j in range(Number_Input2):
    question = input()
    if question in name:
        x.append(name[question])
    else:
        x.append("Not found")
print()
for k in x:
    print(k)