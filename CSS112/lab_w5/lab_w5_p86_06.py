# Input : 1 2 0 2 3 4 5 5
x = [int(i) for i in input().split()]
x.sort()
y = [x[j] for j in range(len(x)-1) if x[j] != x[j+1]]
y.append(x[-1])
print(y)