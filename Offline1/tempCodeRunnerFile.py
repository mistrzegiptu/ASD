def SortH(p,k):
    head = p
    T = []
    while p != None:
        T.append(p)
        p = p.next
    
    for i in range(1, len(T)):
        kCounter = 0
        j = i
        while j > 0 and kCounter < k and T[j].val < T[j-1].val:
            T[j], T[j-1] = T[j-1], T[j]
            j -= 1
            kCounter += 1
    p = T[0]    
    for i in range(len(T)-1):
        p.next = T[i+1]
        p = p.next
        
    T[-1].next = None

    return T[0]