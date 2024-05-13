''' Franciszek Jawor
Rozwiązanie korzysta z algorytmu Dijktry i gdy natrafi na planetę będącą przy osobliwości,
porównuje drogę do każdej z tych planet i dodaje je do kolejki priorytetowej.
Złożoność czasową szacuję na O(E log(V+S))
'''
from zad5testy import runtests
from _collections import defaultdict
import heapq
def spacetravel( n, E, S, a, b ):
    G = defaultdict(list)
    for path in E:
        G[path[0]].append((path[1], path[2]))
        G[path[1]].append((path[0], path[2]))
    pq = []
    heapq.heappush(pq, (0, a))
    dist = [float("inf") for _ in range(n)]
    dist[a] = 0

    while pq:
        d, u = heapq.heappop(pq)
        for v, weight in G[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
        if u in S:
            for v in S:
                if dist[v] > dist[u]:
                    dist[v] = dist[u]
                    heapq.heappush(pq, (dist[v], v))

    if dist[b] == float("inf"):
        return None
    return dist[b]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )