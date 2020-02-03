def dfs(graph, root):
    visited = []
    next_visit = [*graph[root]]

    while next_visit:
        node = next_visit.pop()
        if node not in visited:
            visited.append(node)
            next_nodes = graph[node]
            next_visit.extend(next_nodes)
    return visited


# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     print(start)
#     for next in graph[start] - visited:
#         dfs(graph, next, visited)
#     return visited


if __name__ == '__main__':
    # graph = {'0': set(['1', '2']),
    #          '1': set(['0', '3', '4']),
    #          '2': set(['0']),
    #          '3': set(['1']),
    #          '4': set(['2', '3'])}
    graph = {'0': ['1', '2'],
             '1': ['0', '3', '4', '5', '6'],
             '2': ['0'],
             '3': ['1'],
             '4': ['2', '3'],
             '5': ['2', '4', '6'],
             '6': ['1', '4', '5']}

    print(dfs(graph, '0'))
    # print(dfs(graph, '0'))
