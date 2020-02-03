from collections import deque


def bfs(graph, root):
    visited = []
    q = deque()
    q.append(root)

    while q:
        node = q.popleft()
        for adjacent_node in graph[node]:
            if adjacent_node not in visited:
                visited.append(adjacent_node)
                q.append(adjacent_node)

    return visited


if __name__ == '__main__':
    graph = {'0': ['1', '2'],
             '1': ['0', '3', '4', '5', '6'],
             '2': ['0'],
             '3': ['1'],
             '4': ['2', '3'],
             '5': ['2', '4', '6'],
             '6': ['1', '4', '5']}

    print(bfs(graph, '6'))
