# The code is a binary search algorithm that finds the exponent of 10 that is closest to the input
# number.
import math

a = float(input())
L = 0
U = a
x = (L+U)/2
while not math.isclose(a, 10**x):
    if 10**x > a:
        U = x
    else:
        L = x
    x = (L+U)/2
print(round(x, 6))
