from zad9testy import runtests
def trip(M):
  m = len(M)
  n = len(M[0])
  dp = [[-1] * n for _ in range(m)]

  def dfs(x, y):
    if dp[x][y] != -1:
      return dp[x][y]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_length = 1

    for dx, dy in directions:
      nx, ny = x + dx, y + dy
      if 0 <= nx < m and 0 <= ny < n and M[nx][ny] > M[x][y]:
        max_length = max(max_length, 1 + dfs(nx, ny))

    dp[x][y] = max_length
    return dp[x][y]

  for i in range(m):
    for j in range(n):
      dfs(i, j)

  maxLen = 0
  for i in range(m):
    for j in range(n):
      maxLen = max(maxLen, dp[i][j])

  return maxLen

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( trip, all_tests = True )
