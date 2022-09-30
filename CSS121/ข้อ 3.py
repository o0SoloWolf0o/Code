inf = float("inf")

N = 5
G = [[0, 19, 5, 0, 0],
    [19, 0, 5, 9, 2],
    [5, 5, 0, 1, 6],
    [0, 9, 1, 0, 1],
    [0, 2, 6, 1, 0]]


selected_node = [0, 0, 0, 0, 0]
round_edge = 0
selected_node[0] = True

print("Edge   : Weight")
while (round_edge < N - 1):
    minimum = inf
    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if ((not selected_node[n]) and G[m][n]):  
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(str(a) + " -> " + str(b) + " : " + str(G[a][b]))
    selected_node[b] = True
    round_edge += 1





# https://favtutor.com/blogs/prims-algorithm-python