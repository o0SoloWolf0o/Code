graph = {
    'nodeStart': {'A': 0, 'B': 0},
    'A': {'C': 3, 'D': 3},
    'B': {'E': 4},
    'C': {'F': 2},
    'D': {'nodeFinish': 1},
    'E': {'G': 2},
    'F': {'nodeFinish': 1},
    'G': {'nodeFinish': 1},
}

def find_longest_path(graph, node):
    if node == 'nodeFinish':
        return ['nodeFinish'], 0

    longest = []
    max_distance = float('-inf')

    for neighbor, distance in graph[node].items():
        path, path_distance = find_longest_path(graph, neighbor)
        if path_distance + distance > max_distance:
            longest = path
            max_distance = path_distance + distance

    return [node] + longest, max_distance

path, path_distance = find_longest_path(graph, 'nodeStart')

print("Longest Path:", ' -> '.join(path))
print("Path Distance:", path_distance)