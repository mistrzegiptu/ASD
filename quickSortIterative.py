def quickSort(T, p, r):
    s = []
    s.append((p,r))

    while len(s) > 0:
        p, r = s.pop()
        q = partition(T, p, r)

        if p < q - 1:
            s.append((p, q-1))
        
        if q + 1 < r:
            s.append((q+1, r))

def partition(T, p, r):
    return 0