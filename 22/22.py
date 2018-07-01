def solve(n):
    dp = [0] * (n//2 + 1)
    dp[0] = 1

    for i in range(1, n//2 + 1):
        dp[i] = 0;
        for j in range(0, i):
            dp[i] += dp[j] * dp[i - j - 1]

    return dp[n//2]

print(solve(16))
