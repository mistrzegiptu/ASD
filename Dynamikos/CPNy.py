def Traktor(S, B, L):
    #sprawdzenie odległości między parami
    n = len(S)

    S = [0] + S + [B]
    prev = 0
    counter = 0

    for i in range(1, n):
        if L >= S[i]-S[prev]:
            continue
        else:
            counter += 1
            prev = -1

    return counter


L = 20
d = 105 
S = [1, 9, 21, 30, 35, 39, 41, 42, 50, 58, 62, 80, 85, 90, 92, 97, 98, 100, 105, 112, 130, 135]
fuel = 1
print(Traktor(S, d, L) ) # 7

L = 20
d = 138
S = [1, 9, 21, 30, 35, 39, 41, 42, 50, 58, 62, 80, 85, 90, 92, 97, 98, 100, 105, 112, 135, 140]
fuel = 1
print(Traktor(S, d, L)) # -1

L = 20
d = 20
S = [1, 9, 21, 30, 35, 39, 41, 42, 50, 58, 62, 80, 85, 90, 92, 97, 98, 100, 105, 112, 135, 140]
fuel = L
print(Traktor(S, d, L))# 0

L = 20
d = 132
S = [0, 9, 21, 30, 35, 39, 41, 42, 50, 58, 62, 80, 85, 90, 92, 97, 98, 100, 105, 112, 135, 140]
fuel = 0
print(Traktor(S, d, L)) # 8

L = 20
d = 133
S = [0, 9, 21, 30, 35, 39, 41, 42, 50, 58, 62, 80, 85, 90, 92, 97, 98, 100, 105, 112, 135, 140]
fuel = 0
print(Traktor(S, d, L)) # -1