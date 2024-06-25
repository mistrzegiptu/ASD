'''Franciszek Jawor
Algorytm tworzy tablicę DP, która przechowuje minimalną sumę odległości i biurowców od najbliższych działek,
na początku wypełnia dla pierwszego biurowca odległościami od każdej działki, a następnie
sprawdza czy utworzenie parkingu na poprzedniej działce jest bardziej opłacalne.

Złożoność pamięciową, jak i czasową oceniam na O(n*m)
'''
from zad8testy import runtests

def parking(X,Y):
  n = len(X)
  m = len(Y)

  dp = [[float('inf')] * m for _ in range(n)]
  dp[0][0] = 0

  for j in range(m):
    dp[0][j] = abs(X[0] - Y[j])

  for i in range(0, n):
    for j in range(i, m):
      if j > 0:
        dp[i][j] = min(dp[i][j], dp[i][j - 1])
      dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + abs(X[i] - Y[j]))

  return dp[-1][-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
