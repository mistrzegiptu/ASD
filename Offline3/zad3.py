from zad3testy import runtests
'''Franciszek Jawor
rozwiązanie sprawdza po kolei każdy punkt i zlicza ile punktów dominuje.
Złożoność czasową szacuję na O(n^2), a pamięciową na O(1)
'''
def dominance(P):
  maxDom = 0
  for point1 in P:
    currentDom = 0
    for point2 in P:
      if point1[1] > point2[1] and point1[0] > point2[0]:
        currentDom += 1
    maxDom = max(maxDom, currentDom)
  return maxDom
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )