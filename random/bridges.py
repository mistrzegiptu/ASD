def bridges(G):
    n = len(G)
    low = [0] * n
    times = [0] * n
    time = 0
    bridges = []

    def dfs(u,parent):
        nonlocal times, low, time
        times[u] = times[parent] + 1
        low[u] = times[u]
        for v in G[u]:
            if not times[v]:
                dfs(v, u)
                if low[v] < low[u]:
                    low[u] = low[v]
            elif v != parent:
                if times[v] < low[u]:
                    low[u] = times[v]

        if times[u] == low[u] and parent > -1:
            bridges.append((parent, u))

    for i in range(n):
        if not times[i]:
            dfs(i, -1)

    return bridges


G = [[1, 3], [0, 4], [], [0], [1]]
print(bridges(G))