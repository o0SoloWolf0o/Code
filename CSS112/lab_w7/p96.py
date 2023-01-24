str_input = input()
str_input = str_input.lower()
count = {}
for i in str_input:
    if i.isalpha() == True :
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
x = []
for j in count:
    x.append([-count[j], j])
x.sort()
for k , j in x:
    print(j,'->',-k)