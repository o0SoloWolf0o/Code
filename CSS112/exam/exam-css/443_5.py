switches = str(input())
counts = 0
for i in range(len(switches)-1):
    if switches[i] != switches[i+1]:
        counts += 1
print(counts)