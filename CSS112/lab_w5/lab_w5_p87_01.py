# Input : int number เลขจำนวนเต็ม
n = int(input())
x = [j for i in range(2, n//2) for j in range(2*i, n-1, i)]
x.sort()
y = [x[j] for j in range(len(x)-1) if x[j] != x[j+1]]
y.append(x[-1])
z = [i for i in range(2, n) if i not in y]
print(z)