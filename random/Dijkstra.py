from queue import PriorityQueue

def dijkstra(G,s):
    n = len(G)
    dist = [float('inf')] * n

    dist[s] = 0

    pq = PriorityQueue()
    pq.put((s,0))

    while not pq.empty():
        u, d = pq.get()

        for v, distance in G[u]:
            if dist[u] + distance < dist[v]:
                dist[v] = dist[u] + distance
                pq.put((v, dist[v]))

    return dist