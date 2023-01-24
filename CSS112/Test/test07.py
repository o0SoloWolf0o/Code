N = int(input())
Answer = list(input())
scores = [0,0,0]
Adrian = ['A','B','C']
Bruno = ['B','A','B','C']
Goran = ['C','C','A','A','B','B']

for i in range(N):
    if Answer[i] == Adrian[i%3]:
        scores[0] += 1
    if Answer[i] == Bruno[i%4]:
        scores[1] += 1
    if Answer[i] == Goran[i%6]:
        scores[2] += 1

print(max(scores))

for i in range(3):
    if scores[i] == max(scores):
        if i == 0:
            print('Adrian')
        elif i == 1:
            print('Bruno')
        elif i == 2:
            print('Goran')