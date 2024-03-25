import math

from zad3testy import runtests

def heapify(T, n, i, coord):
  l = 2 * i + 1
  r = 2 * i + 2
  maxInd = i

  if l < n and T[l][coord] < T[maxInd][coord]:
    maxInd = l
  if r < n and T[r][coord] < T[maxInd][coord]:
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
'''def dominance(P):
  heapSort(P, 0)
  dominant = P[0]
  for i in range(len(P)):
      if P[i][1] > dominant[1]:
        dominant = P[i]
  count = 0
  for i in range(len(P)):
      if P[i][0] < dominant[0] and P[i][1] < dominant[1]:
          count += 1
  return count'''
'''def dominance(P):
  maxDomina = 0
  heapSort(P,0)
  for i in range(len(P)//2):
    currentDomina = 0
    for j in range(i+1,len(P)):
      if P[i][0] > P[j][0] and P[i][1] > P[j][1]:
        currentDomina += 1
    maxDomina = max(maxDomina, currentDomina)
  return maxDomina'''
def dominance(P):
  maxDomina = 0
  for point1 in P:
    currentDomina = 0
    for point2 in P:
      if point1[1] > point2[1] and point1[0] > point2[0]:
        currentDomina += 1
    maxDomina = max(maxDomina, currentDomina)
  return maxDomina

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
