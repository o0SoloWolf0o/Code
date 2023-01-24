number = int(input())
for i in range(number):
    a = int(input())
    if a == 2 or a%2 == 1:
        print("T")
    else:
        print("F")