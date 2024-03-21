from zad3testy import runtests

def dominance(P):
  maxDomina = 0
  for i in range(len(P)):
    currentDomina = 0
    for j in range(len(P)):
      if P[i][0] > P[j][0] and P[i][1] > P[j][1]:
        currentDomina += 1
    maxDomina = max(maxDomina, currentDomina)

  return maxDomina

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
