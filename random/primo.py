from queue import PriorityQueue

def primo(G, s):
    n = len(G)
    parents = [None] * n
    mins = [float("inf")] * n
    visited = [False] * n
    counter = 0
    pq = PriorityQueue()
    pq.put((0,s))

    while counter < n:
        u = pq.get()[1]

        if not visited[u]:
            for v, d in G[u]:
                if not visited[v]:
                    if mins[v] > d:
                        mins[v] = d
                        parents[v] = u
                        pq.put((d, v))
            visited[u] = True
            counter += 1

    return parents

G = [[(1,8), (2,5)], [(0,8), (3,3)], [(0,5), (3,2), (4,6)], [(1,3), (2,2), (4,9)], [(2,6), (3,9)]]
print(primo(G, 2))