from zad3testy import runtests

def heapify(T, n, i, coord):
  l = 2 * i + 1
  r = 2 * i + 2
  maxInd = i

  if l < n and T[l][coord] > T[maxInd][coord]:
    maxInd = l
  if r < n and T[r][coord] > T[maxInd][coord]:
    maxInd = r
  if maxInd != i:
    T[maxInd], T[i] = T[i], T[maxInd]
    heapify(T, n, maxInd, coord)

def buildHeap(T, coord):
  n = len(T)
  for i in range((n-2)//2, -1, -1):
    heapify(T, n, i, coord)
def heapSort(T, coord):
  n = len(T)
  buildHeap(T, coord)
  for i in range(n-1, 0, -1):
    T[i], T[0] = T[0], T[i]
    heapify(T, i, 0, coord)
def dominance(P):
  heapSort(P, 0)
  #print(P)
  heapSort(P, 1)
  #print(P)
  dominant = P[-1]
  count = 0
  for i in range(len(P)):
      if P[i][0] < dominant[0] and P[i][1] < dominant[1]:
          count += 1
  return count

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
