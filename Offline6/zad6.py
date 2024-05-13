from zad6testy import runtests
from _collections import defaultdict
import heapq

def jumper( G, s, w ):
    n = len(G)
    graph = defaultdict(list)
    jumps = []

    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                graph[2*i].append((2*j, G[i][j]))

        for j in range(n):
            if G[i][j] != 0:
                for k in range(n):
                    if k != i and G[j][k] != 0:
                        graph[2*i+1].append((2*k+1, max(G[i][j], G[j][k])))
                        jumps.append((i, k))

    '''for i in range(n):
        for j in range(i+1, n):
            if G[i][j] != 0:
                graph[i].append((j, G[i][j]))
                graph[j].append((i, G[i][j]))
                for k in range(j+1, n):
                    if G[j][k] != 0 and i != k:
                        jumps.append((i, k))
                        jumps.append((k, i))
                        graph[i].append((k, max(G[i][j], G[j][k])))
                        graph[k].append((i, max(G[i][j], G[j][k])))'''

    pq = []
    dist = [float("inf") for _ in range(n)]
    dist[s] = 0

    heapq.heappush(pq, (0, s*2, False))

    while pq:
        d, u, jump = heapq.heappop(pq)
        for v, weight in graph[u]:
            if u % 2 == 1 and jump:
                continue
            elif u % 2 == 1:
                jump = True
            else:
                jump = False

            if dist[v//2] > dist[u//2] + weight:
                dist[v//2] = dist[u//2] + weight
                heapq.heappush(pq, (dist[v//2], v, jump))

    return dist[w]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )