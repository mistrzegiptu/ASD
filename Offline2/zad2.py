from zad2testy import runtests
''' Franciszek Jawor
Algorytm tworzy p elementową tablicę i umieszcza tam p początkowych wartości
z głównej tablicy, następnie sortuje ją korzystając z heap sorta O(plogp)
Następnie dodaje do sumy k-ty największy element i iteruje od indeksu p 
do końca głównej tablicy, usuwając i-ty element, a dodając p+i z zachowaniem
rosnącej kolejności.
Złożoność pamięciową algorytmu oceniam na O((n-p)p), 
natomiast czasową na O(p) 
'''
def heapify(T, n, i):
    l = 2 * i + 1
    r = 2 * i + 2
    maxInd = i

    if l < n and T[l] > T[maxInd]:
        maxInd = l
    if r < n and T[r] > T[maxInd]:
        maxInd = r
    if maxInd != i:
        T[i], T[maxInd] = T[maxInd], T[i]
        heapify(T, n, maxInd)

def buildHeap(T):
    n = len(T)
    for i in range((n-2)//2, -1, -1):
        heapify(T, n, i)

def heapSort(T):
    n = len(T)
    buildHeap(T)
    for i in range(n-1, 0, -1):
        T[i], T[0] = T[0], T[i]
        heapify(T, i, 0)
def getIndex(T, x):
    left = 0
    right = len(T)-1
    while left <= right:
        mid = (left+right)//2
        if T[mid] == x:
            return mid
        elif T[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left

def ksum(T, k, p):
    n = len(T)
    resultSum = 0
    A = [0 for i in range(p)]

    for i in range(p):
        A[i] = T[i]
    heapSort(A)

    l = 0
    for i in range(p, n):
        resultSum += A[p-k]
        x = T[i]
        index = getIndex(A, T[l])
        A.pop(index)
        #I'm an idiot...
        '''j = 0
        while j < p-1 and A[j] < x:
            j += 1
        A.insert(j, x)'''
        A.insert(getIndex(A, x), x)
        l += 1
    return resultSum+A[p-k]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
