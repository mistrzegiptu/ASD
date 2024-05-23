def directed_graph_list(E, n):
    G = [[] for _ in range(n)]
    for edge in E:
        G[edge[0]].append(edge[1])
    return G
def get_process_times(G):
    n = len(G)
    times = [0] * n
    visited = [False] * n
    time = 0

    def dfs(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs(v)
        nonlocal time
        time += 1
        times[u] = time

    for u in range(n):
        if not visited[u]:
            dfs(u)

    return times


def get_transposed_graph(G):
    n = len(G)
    G2 = [[] for _ in range(n)]

    for u in range(n):
        for v in G[u]:
            G2[v].append(u)

    return G2


def get_vertices_order(times):
    n = len(times)
    order = [-1] * n
    for i in range(n):
        order[n - times[i]] = i
    return order


def find_coherent_components(G):
    n = len(G)
    times = get_process_times(G)
    G = get_transposed_graph(G)
    order = get_vertices_order(times)
    result = [-1] * n
    token = 0

    def dfs(u):
        result[u] = token
        for v in G[u]:
            if result[v] < 0:
                dfs(v)

    for i in range(n):
        u = order[i]
        if result[u] < 0:
            dfs(u)
            token += 1

    return result

edges = [
        [1, 3], [1, 4], [2, 1], [3, 2], [4, 5]
    ]
G = directed_graph_list(edges, 6)
print(find_coherent_components(G))