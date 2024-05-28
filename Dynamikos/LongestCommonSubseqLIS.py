def LIS(T):
    dp = [float('inf')] * (len(T) + 1)
    dp[0] *= -1

    for x in T:
        l, r, ans = 0, len(T) + 1, 0
        while l <= r:
            mid = (l + r) // 2
            if dp[mid] > x:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        if dp[ans - 1] < x:
            dp[ans] = x

    for i in range(len(T), 0, -1):
        if dp[i] != float('inf'):
            return i

    return 0