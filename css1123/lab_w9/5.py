import numpy as np
k = int(input())
arr = np.zeros((k,k),int)
arr[::2, 1::2] = arr[1::2, ::2] = 1
print(arr)