''' Franciszek Jawor
Algorytm buduje min kopiec o wielkości k+1, dodaje najmniejszy element z kopca na początek listy i usuwa go z kopca, 
następnie dodaje do kopca kolejny element z listy i znowu tworzy min kopiec, aż do wyczerpania listy. 
Dzięki temu wybiera po kolei najmniejsze elementy i sortuje listę. Rozwiązanie to
ma złożoność czasową n log(k)
k = Θ(1) O(n)
k = Θ(log n) O(n log(log(n)))
k = Θ(n) O(n log(n))
'''

from zad1testy import Node, runtests

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def parent(i):
    return (i-1)//2

def heapify(A, i, n):
    l = left(i)
    r = right(i)
    max_ind = i

    if l < n and A[l].val < A[max_ind].val:
        max_ind = l
    if r < n and A[r].val < A[max_ind].val:
        max_ind = r

    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, max_ind, n)

def build_heap(A):
    n = len(A)
    for i in range(parent(n-1), -1, -1):
        heapify(A, i, n)


def SortH(p, k):
    head = Node()
    result = head
    heap = []

    while len(heap) <= k: 
        heap.append(p)
        p = p.next

        if p.next is None: 
            break
        
    build_heap(heap)

    while heap:
        result.next = heap[0]
        result = result.next
        result.next = None

        if p is not None:
            heap.append(p)
            p = p.next

        heap[0] = heap[-1]
        heap.pop()
        heapify(heap, 0, len(heap))

    return head.next


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
