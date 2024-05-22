def topologicalSort(G):
    L = []
    visited = [False] * len(G)

    def dfs(G, u):
        nonlocal visited, L
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                dfs(G, v)

        L.append(u)

    for i in range(len(G)):
        if not visited[i]:
            dfs(G, i)
    return L


G = [[1], [2], [], [1,2]]
result = topologicalSort(G)
result.reverse()
print(result)