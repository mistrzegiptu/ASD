T = [(2,3), (11,5), (6, 13)]

def countSort(T, p, m):
    countTab = [0 for _ in range(m)]
    for x in T
        countTab[x[p]] += 1
    for i in range(1, m):
        countTab[i] += countTab[i-1]
    
    result = [None for _ in range(len(T))]
    
    for i in range(len(T)-1, -1, -1):
        result[countTab[T[i][p]]-1] = T[i]
        countTab[T[i][p]] -= 1
    
    return result

def nSquareSort(T):
    n = len(T)
    Tab = [None for _ in range(n)]
    
    for i in range(n):
        c1 = T[i]//4
        c2 = T[i]%4
        Tab[i] = (c1, c2)
    Tab = countSort(Tab, 1, m)
    Tab = countSort(Tab, 0, m)
    
    for i in range(n):
        T[i] = Tab[i][0] * 4 + Tab[i][1]
    
    return T