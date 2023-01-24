str_in1 = input().split()
str_in2 = input()
a = 1
for i in range(len(str_in1)):
    if str_in2 == str_in1[i]:
        str_in1[i] = str(a)
        a+=1
print(*str_in1)