import math

n = int(input())
a = math.sqrt(2*(math.pi)) * (n**(n) + 1 / 2) * math.e**((-n) + (1 / (12 * n + 1)))
b = math.sqrt(2*(math.pi)) * (n**(n) + 1 / 2) * math.e**((-n) + (1 / (12 * n)))
print(a)
print(b)
