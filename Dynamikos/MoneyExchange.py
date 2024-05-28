def money(nom, k):
  dp = [float('inf') for i in range(k+1)]
  dp[0]=0
  for i in range(1, k+1):
    for x in nom:
      if i-x >= 0:
        dp[i] = min(dp[i], dp[i-x]+1)

  return dp[k]

print(money([1,2,5,7],21))