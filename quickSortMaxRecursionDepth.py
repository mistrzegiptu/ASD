def sort(T, p, r):
    while p < r:
        q = partition(T, p, q-1)
        
        if q > (p+r)//2:
            sort(T, q+1, r)
        else:
            sort(T, p, q-1)
            p = q + 1

def partition():
    return 0