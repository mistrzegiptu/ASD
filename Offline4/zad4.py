'''Franciszek Jawor
Algorytm przeszukuje graf za pomocą DFS zaczynając od wierzchołka x,
następnie oblicza aktualny minimalny i maskymalny pułap dla obecnego wierzchołka
i sprawdza czy możliwy jest przelot między nimi. Taki wybór minimalizuje ilość
wierchołków do przetworzenia, co przyśpiesza działanie algorytmu
Złożoność pesymistyczną szacuję na O(n!)
'''
from zad4testy import runtests
from collections import defaultdict

def Flight(L,x,y,t):
  G = defaultdict(list)

  for path in L:
    G[path[0]].append((path[1], path[2]))
    G[path[1]].append((path[0], path[2]))
  visited = [0] * (max(G.keys())+1)
  visited[x] = 1
  def DFS(vert, minCost, maxCost):
    nonlocal visited
    visited[vert] = 1
    if vert == y:
      return True
    for v in G[vert]:
      mini = min(minCost, v[1])
      maxi = max(maxCost, v[1])
      if maxi - mini <= 2 * t and visited[v[0]] == 0:
        if DFS(v[0], mini, maxi):
          return True
    visited[vert] = 0
    return False

  for v in G[x]:
    visited = [0 for _ in range(len(visited))]
    visited[x] = 1
    if DFS(v[0], v[1], v[1]):
      return True

  return False

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(Flight, all_tests = True)