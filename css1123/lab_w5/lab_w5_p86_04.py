# Input : 1 2 3
x = [int(i) for i in input().split()]
# Input : 4 5 6
y = [int(i) for i in input().split()]
z = [x[j]+y[j] for j in range(len(x))]
print(z)