''' Franciszek Jawor
Rozwiązanie wykorzystuje algorytm Dijkstry szukając najpierw najkrótszej ścieżki ze startu do każdego roweru,
a następnie od mety do każdego roweru, potem wyszukuje najkrótszą trasę calkowitą
Złożoność obliczeniową oceniam na O(ElogV)
'''

from egz1atesty import runtests
from _collections import defaultdict
from _heapq import *
def armstrong( B, G, s, t):
  n = len(G)
  graph = defaultdict(list)

  for u, v, c in G:
    graph[u].append((v, c))
    graph[v].append((u, c))

  def Dijsktra(s):
    dist = [float('inf')] * n
    dist[s] = 0
    p = []
    heappush(p, (s, 0))

    while p:
      u, c = heappop(p)

      for v, cost in graph[u]:
        if dist[v] > dist[u] + cost:
          dist[v] = dist[u] + cost
          heappush(p, (v, cost))

    return dist

  m = len(B)
  minDist = float('inf')
  walk = Dijsktra(s)
  ride = Dijsktra(t)
  for i in range(m):
    bikeV, p, q = B[i]
    if p >= q: #pomijamy niewygodne rowery oraz p == q, bo wtedy rower nie wpływa na wynik
        continue
    currDist = walk[bikeV] + ride[bikeV] * p // q
    minDist = min(minDist, currDist)

  return min(minDist, walk[t])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )
