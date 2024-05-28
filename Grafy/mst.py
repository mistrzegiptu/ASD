G = []
n = len(G)
parent = [i for i in range(n)]
rank = [0 for _ in range(n)]


def find_set(x):
    if x != parent[x]:
        find_set(parent[x])
    return parent[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1
