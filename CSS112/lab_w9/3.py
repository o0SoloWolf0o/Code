import numpy as np
M = np.array([[3,2],[5,6],[7,1]])
Max = np.max(M, axis=0)
Min = np.min(M, axis=0)
x = Max - Min
print(x)