''' Franciszek Jawor
Algorytm sprawdza wszystkie możliwe podciągi podanego ciągu i dodaje je do tablicy
tab w posortowanej kolejności, z użyciem binary searcha. Następnie sprawdza czy
w pierwszych k-elementach nie znajdują się liczby dodatnie i zlicza ich ewentualną sumę,
potem zlicza sumę tablicy tab bez k najmniejszych elementów i dodaje ewentualną sumę
policzoną wcześniej.

Złożoność obliczeniową oceniam na O(k*n^2 *logn)
'''

from egz1btesty import runtests


def getIndex(T, x): # Funkcja do binary searcha, w przypadku nie znalezienia elemntu zwraca miejsce w tablicy, do którego trzeba go wstawić
  left = 0
  right = len(T) - 1
  while left <= right:
    mid = (left + right) // 2
    if T[mid] == x:
      return mid
    elif T[mid] < x:
      left = mid + 1
    else:
      right = mid - 1
  return left

def kstrong( T, k):
  n = len(T)
  maxSum = 0
  for i in range(n):
    tab = []
    for j in range(i,n):
      tab.insert(getIndex(tab, T[j]), T[j])
      kPlus = 0
      m = len(tab)
      for l in range(min(k, m)): #zliczanie ewentualnej sumy dodatnich elementów z początku
        if tab[l] > 0:
          kPlus += tab[l]
      maxSum = max(maxSum, sum(tab[k:m])+kPlus)

  return maxSum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )
