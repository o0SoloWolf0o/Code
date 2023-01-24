# Input : -1 -2 1 2 3 4 5
x = [int(y) for y in input().split()]
x = [y for y in x if y <= 0]
z = len(x)
print(z)
