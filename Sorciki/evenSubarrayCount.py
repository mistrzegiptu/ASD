#NIE DZIAŁA XD

def count(T):
    n = len(T)
    cnt = 0
    Sp = [None]*(n+1)
    O = [0]*(n+1)
    E = [0]*(n+1)
    Sp[0] = 0
    S = 0
    for i in range(n):
        S += T[i]
        Sp[i+1] = S
    odd = 0
    even = 0
    for j in range(n+1):
        if Sp[j] % 2 == 0:
            even += 1
        else:
            odd += 1
        O[j] = odd
        E[j] = even
    
    for k in range(n+1):
        if Sp[k] % 2 == 0:
            cnt += E[k]
        else:
            cnt += O[k]
    
    return cnt

print(count([2,9,113,72,10,18,14]))
