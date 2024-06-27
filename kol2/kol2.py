from kol2testy import runtests
from _collections import defaultdict
import heapq
def warrior( G, s, t):
    graph = defaultdict(list)
    for u, v, w in G:
        graph[u].append((v, w))
        graph[v].append((u, w))

    MAX_NO_REST_TIME = 16
    REST_TIME = 8

    def add_edge(expanded_graph, u, v, u_tired, v_tired, weight):
        if v_tired <= MAX_NO_REST_TIME:
            expanded_graph[(u, u_tired)].append(((v, v_tired), weight))

    expanded_graph = defaultdict(list)
    for u in graph:
        for v, w in graph[u]:
            for u_tired in range(MAX_NO_REST_TIME + 1):
                v_tired = u_tired + w
                if v_tired > MAX_NO_REST_TIME:
                    v_tired = w
                    add_edge(expanded_graph, u, v, u_tired, v_tired, w + REST_TIME)
                else:
                    add_edge(expanded_graph, u, v, u_tired, v_tired, w)

    pq = []

    dist = defaultdict(lambda: float('inf'))

    heapq.heappush(pq, (0, (s, 0)))  # (total_travel_time, (vertex, tired))
    dist[(s, 0)] = 0

    while pq:
        total_travel_time, (vertex, tired) = heapq.heappop(pq)

        if vertex == t:
            return total_travel_time

        for (neighbor, neighbor_tired), weight in expanded_graph[(vertex, tired)]:
            new_total_travel_time = total_travel_time + weight
            if new_total_travel_time < dist[(neighbor, neighbor_tired)]:
                dist[(neighbor, neighbor_tired)] = new_total_travel_time
                heapq.heappush(pq, (new_total_travel_time, (neighbor, neighbor_tired)))

    return float('inf')

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )
