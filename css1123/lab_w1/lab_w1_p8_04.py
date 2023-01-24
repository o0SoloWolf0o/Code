import math

r,theta = (*map(int,input("Enter : ").split( )),)

x = r*math.cos(theta)
y = r*math.sin(theta)
print(x,y)