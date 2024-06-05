from zad7testy import runtests

def maze(L):
    n = len(L)
    if L[0][0] == '#' or L[n - 1][n - 1] == '#':
        return -1

    dp = [[0] * n for _ in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(n):
            if L[i][j] == '#':
                continue
            if i > 0 and dp[i - 1][j] > 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + 1)
            if j > 0 and dp[i][j - 1] > 0:
                dp[i][j] = max(dp[i][j], dp[i][j - 1] + 1)
            if i < n - 1 and dp[i + 1][j] > 0:
                dp[i][j] = max(dp[i][j], dp[i + 1][j] + 1)

    result = dp[n - 1][n - 1]
    return result - 1 if result > 0 else -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = False )
