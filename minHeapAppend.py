class heap:
    def __init__(self, max_size):
        self.T = [None for _ in range(max_size)]
        self.max_size = max_size
        self.size = 0

def heapAdd(H, x):
    if H.size < H.max_size:
        increaseHeap(H.T, H.size, x)
        H.size += 1

def parent(n):
    if n == 0:
        return 0
    else:
        return (n-1)//2
    
def increaseHeap(T, i, x):
    T[i] = x
    while T[parent(i)] > T[i]:
        T[parent(i)], T[i] = T[i], T[parent(i)]
        i = parent(i)