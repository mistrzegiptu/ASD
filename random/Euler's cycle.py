def eulers(G):
    n = len(G)
    visited = [[False] * n for _ in range(n)]
    result = []

    def dfs(u):
        for v in G[u]:
            if not visited[u][v]:
                visited[u][v] = visited[v][u] = True
                dfs(v)

        result.append(u)

    dfs(0)
    return result


G = [[1, 4], [0, 2, 3, 4], [1, 3], [1, 2, 4, 5], [0, 1, 3, 5], [3, 4]]
print(eulers(G))