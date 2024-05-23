def minDistance(G, dist, sptSet):
    n = len(G)
    min = float('inf')

    for u in range(n):
        if dist[u] < min and sptSet[u] == False:
            min = dist[u]
            min_index = u

    return min_index

def Dijsktra(G, s):
    n = len(G)
    dist = [float('inf')] * n
    visited = [False] * n
    dist[s] = 0

    for _ in range(n):
        x = minDistance(G, dist, visited)
        visited[x] = True

        for y in range(n):
            if G[x][y] > 0 and visited[y] == False and dist[y] > dist[x] + G[x][y]:
                dist[y] = dist[x] + G[x][y]

    return dist

G = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
   [4, 0, 8, 0, 0, 0, 0, 11, 0],
   [0, 8, 0, 7, 0, 4, 0, 0, 2],
   [0, 0, 7, 0, 9, 14, 0, 0, 0],
   [0, 0, 0, 9, 0, 10, 0, 0, 0],
   [0, 0, 4, 14, 10, 0, 2, 0, 0],
   [0, 0, 0, 0, 0, 2, 0, 1, 6],
   [8, 11, 0, 0, 0, 0, 1, 0, 7],
   [0, 0, 2, 0, 0, 0, 6, 7, 0]
   ]
print(Dijsktra(G, 0))

