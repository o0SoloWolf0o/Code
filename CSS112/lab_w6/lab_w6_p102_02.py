x = int(input())
t = tuple()
while x > 0:
    t = (x%10,) + t
    x = x//10
print(t)