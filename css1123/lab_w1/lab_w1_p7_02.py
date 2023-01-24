import math


x = int(input("Enter a number: "))
y = 2 - x + 3/7*(x**2) - 5/11*(x**3) + math.log(x,10)
print(y)