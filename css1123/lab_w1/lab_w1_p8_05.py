import math

x,y = (*map(int,input("Enter :").split( )),)
r = math.sqrt(x**2 + y**2)
# theta = math.atan(y/x)
theta = math.atan2(y,x) 
print(r,theta)