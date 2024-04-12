#Franciszek Jawor
''' Algorytm idzie od końca tablicy i wykonuje na niej partycjonowanie Lomuto. Tym samym wyszukuje indeks,
na którym znajduje się dany element, co również oznacza jego rangę. Warunkiem końcowym jest znalezienie
elementu, który po partycjonowaniu znajduje się na pierwotnym indeksie. Wówczas jest to maksymalny
rangą element

Złożoność czasową szacuję na O(n^2), ze względu na złożoność partycjonowania O(n) i wywoływanie go O(n) razy
Złożoność pamięciową szacuję na O(n) ze względu na tworzenie kopii tablicy ( o ile python wywołuje free po zakończeniu pętli, jeśli nie, to wówczas jest O(n^2) :( )
'''

from kol1testy import runtests
def partition(A, p, r):
  x = A[r]
  i = p-1
  for j in range(p, r):
    if A[j] < x:
      i += 1
      A[i], A[j] = A[j], A[i]
  A[i+1], A[r] = A[r], A[i+1]
  return i+1

def maxrank(T):
  maximumRank = 0
  n = len(T)
  for i in range(n-1,-1,-1):
    A = T[:i+1]
    maximumRank = max(maximumRank, partition(A, 0, i))
    if maximumRank == i:
      return maximumRank
  return maximumRank

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )
