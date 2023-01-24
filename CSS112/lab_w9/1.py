import numpy as np
M = np.array([[1,2],[3,4]])
k = int(input())
for i in range(0, len(M)):
    for j in range(0, len(M[i])):
        if i % k == 0 and j % k == 0:
            M[i][j] = 0
print(M)