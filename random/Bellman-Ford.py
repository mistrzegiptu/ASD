def BellmanFord(G, s):
    n = len(G)
    dist = [float('inf')] * n
    dist[s] = 0

    for i in range(n-1):
        for u in range(n):
            for v, d in G[u]:
                if dist[u] + d < dist[v]:
                    dist[v] = dist[u] + d

    for v in range(n):
        for u, d in G[v]:
            if dist[u] > dist[v] + d:
                return False

    return dist