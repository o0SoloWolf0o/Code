binary1 , binary2 = input().split()
integer1 = int(binary1, 2)
integer2 = int(binary2, 2)
integer3 = integer1 + integer2
binary3 = bin(integer3)[2:]
print(binary3)