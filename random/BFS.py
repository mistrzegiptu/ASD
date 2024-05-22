import queue

def BFS(G,s):
    n = len(G)
    q = queue.Queue()
    visited = [False] * n
    d = [-1] * n
    visited[s] = True
    d[s] = 0
    q.put(s)

    while not q.empty():
        v = q.get()
        for u in G[v]:
            if not visited[u]:
                visited[u] = True
                q.put(u)
                d[u] = d[v]+1

    return d


G = [[1, 3], [0, 2], [1, 4], [0], [2]]
print(BFS(G, 0))