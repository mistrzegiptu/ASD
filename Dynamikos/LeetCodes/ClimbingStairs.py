def minCostClimbingStairs(self, cost):
    n = len(cost)
    dp = [float('inf')] * n
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

    return min(dp[n - 1], dp[n - 2])