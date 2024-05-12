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
                graph[i].append((j, G[i][j]))
                graph[j].append((i, G[i][j]))
                for k in range(n):
                    if G[j][k] != 0:
                        jumps.append((i, k))
                        jumps.append((k, i))
                        graph[i].append((k, max(G[i][j], G[j][k])))
                        graph[k].append((i, max(G[i][j], G[j][k])))
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = False )