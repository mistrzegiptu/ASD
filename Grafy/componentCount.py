def component(G):
    visited = [0] * len(G)

    def DFS(G, v):
        nonlocal visited
        visited[v] = 1

        for u in G[v]:
            if visited[u] == 0:
                DFS(G, u)

    DFS(G, 0)

    counter = 1
    for i in range(len(visited)):
        if visited[i] == 0:
            counter += 1
            DFS(G, i)

    return counter

G=[[3,4],[3,5],[3,5],[0,1,2],[0],[1,2]]
print(component(G))
G=[[2,3,4],[],[0,4],[0,4],[0,2,3]]
print(component(G))
G=[[1,2],[0,2],[0,1],[4,5],[3,5],[3,4],[7],[6]]
print(component(G))
G=[[1],[0,2],[1,3],[2,4,7],[3,5],[4],[7],[3,6]]
print(component(G))