a, b, c = [int(z) for z in input().split()]
if b - a >= c - b:
    print(b - a - 1)
else:
    print(c - b - 1)
