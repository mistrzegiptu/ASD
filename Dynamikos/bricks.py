def bricks(T):
  n = len(T)
  DP = [1] * n

  for i in range(1, n):
    a1, b1 = T[i]
    for j in range(i):
      a2, b2 = T[j]
      if a2 <= a1 and b1 <= b2:
        DP[i] = max(DP[i], DP[j] + 1)

  return n - max(DP)


T = [[0, 5], [1, 4], [-3, 7], [2, 3], [2, 6], [4, 6], [2, 3]]
print(bricks(T))
