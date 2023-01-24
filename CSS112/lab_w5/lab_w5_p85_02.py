# Input : 2 1 3 4 5 6 7 8 10 9
x = [int(y) for y in input().split()]
x = [y for y in x if y >= 0]
print(x)
