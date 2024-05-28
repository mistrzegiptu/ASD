'''

'''

def SumSubseq(A, T):
    n = len(A)
    F = [[False] * n for _ in range(T+1)]

    for i in range(n):
        F[0][i] = True

    for i in range(1, n):
        for j in range(T+1):
            F[j][i] = F[j][i] or F[j][i-1]
            if j - A[i] >= 0:
                F[j][i] = F[j][i] or F[j - A[i]][i-1]

    return F[T][n-1]


print(SumSubseq([3, 0, 5, 2, 7, 13, 8], 10))