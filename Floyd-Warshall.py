'''
ALgorytm obliczający tapniecie przechodnie grafu reprezentowanego w postaci macierzowej
Dla każdych 2 wierzchołków u i v ma zaznaczoną krawędź z u do vwtw. gdy w grafie istnieje ścieżka z u do v
'''
G = []
n = len(G)
M = [[G[i][j]] for j in range(n) for i in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            M[i][j] = M[i][j] or (M[i][k] and M[k][j])
            max(M[i][j], min(M[i][k], M[k][j]))