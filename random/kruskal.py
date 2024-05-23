def kruskal(G):
    n = len(G)
    parent = [i for i in range(n)]
    rank = [0] * n

    def find(x):
        nonlocal parent
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        nonlocal parent, rank
        x = find(x)
        y = find(y)

        if rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[x] = y
            if rank[x] == rank[y]:
                rank[y] += 1


    G.sort(key = lambda x: x[2])
    MST = []
    for edge in G:
        x = edge[0]
        y = edge[1]

        parX = find(x)
        parY = find(y)

        if parX != parY:
            MST.append(edge)
            union(x, y)

    return MST