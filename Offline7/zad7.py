''' Franciszek Jawor
W tym algorytmie wykorzystuje 2 tablice, Up przechowuje maksymalną liczbę komnat, która można odwiedzić przychodząc z lewej lub z góry,
a Down- przychodząc z lewej lub z dołu. Algorytm przechodzi przez wszystkie komnaty i aktualizuje obie tablice, biorąc maksymalną
ilość komnat możliwą do odwiedzenia na danym kroku.

Złożoność pamięciową i czasową oceniam na O(n^2)
'''
from zad7testy import runtests

def maze(L):
    n = len(L)

    Up = [[0] * n for _ in range(n)]
    Down = [[0] * n for _ in range(n)]

    #looking for wrong chambers
    for j in range(n):
        for i in range(n):
            if L[i][j] == '#':
                Up[i][j] = -float('inf')
                Down[i][j] = -float('inf')

    #starting values
    for i in range(1, n):
        Up[i][0] += Up[i-1][0] + 1
        Up[0][i] += Up[0][i-1] + 1
        Down[i][0] = -float('inf')
        Down[0][i] += Down[0][i-1] + 1

    for i in range(1, n):

        if(L[0][i] != '#'):
            Up[0][i] = max(Up[0][i-1], Down[0][i-1]) + 1

        if (L[n-1][i] != '#'):
            Down[n-1][i] = max(Up[n-1][i - 1], Down[n-1][i - 1]) + 1

        for j in range(1, n):
            if(L[j][i] == '#'):
                continue
            Up[j][i] = max(Up[j][i-1], Down[j][i-1], Up[j-1][i]) + 1

        for j in range(n-2, -1, -1):
            if(L[j][i] == '#'):
                continue
            Down[j][i] = max(Up[j][i-1], Down[j][i-1], Down[j+1][i]) + 1

    if Up[n-1][n-1] == -float('inf') and Down[n-1][n-1] == -float('inf'):
        return -1
    return Up[n-1][n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
