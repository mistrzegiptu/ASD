import heapq

def dijsktra(G, start, n):
    dist = [float('inf') for _ in range(n)]

    pq = []
    heapq.heappush(pq, (0, start))
    dist[start] = 0

    while pq:
        d, u = heapq.heappop(pq)

        for v, weight in G[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))