from random import randint
def sort(T, p, r):
    while p < r:
        q = partition(T, p, r)
        
        if q > (p+r)//2:
            sort(T, q+1, r)
            r = q - 1
        else:
            sort(T, p, q-1)
            p = q + 1

def partition(T, p, r):
    x= T[r]
    i = p-1

    for j in range(p, r):
        if T[j] < x:
            i += 1
            T[i], T[j] = T[j], T[i]

    T[i+1], T[r] = T[r], T[i+1]
    return i+1

A = [randint(1, 50) for _ in range(11)]

print(A)
sort(A, 0, len(A)-1)
print(A)