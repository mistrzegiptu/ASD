def DFS(G, u, visited, end):
    if visited[u]:
        return False
    if u == end:
        return True
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            if DFS(G, v, visited, end):
                return True

    visited[u] = False
    return False


G = [[1, 3], [0, 2], [1, 4], [0], [2]]
n = len(G)
visited = [False] * n
print(DFS(G, 0, visited, 4))