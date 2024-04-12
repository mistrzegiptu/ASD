from queue import Queue

def isBipartite(G, startV):
    colors = [-1 for _ in range(len(G))]
    colors[startV] = 0

    queue = Queue()
    queue.put(startV)

    while not queue.empty():
        v = queue.get()

        for u in G[v]:
            if colors[u] == -1:
                queue.put(u)
                colors[u] = (colors[v] + 1) % 2
            else:
                if colors[u] == colors[v]:
                    return False

    return True

G=[[3,4],[3,5],[3,5],[0,1,2],[0],[1,2]]
print(isBipartite(G,0))
print(isBipartite(G,4))
G=[[2,3,4],[2,3],[0,1,4],[0,1,4],[0,2,3]]
print(isBipartite(G,1))
print(isBipartite(G,3))