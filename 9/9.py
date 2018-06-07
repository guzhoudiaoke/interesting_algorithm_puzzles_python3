def solve():
    girls, boys = 10, 20

    dp = [ [0 for _ in range(boys+1)] for _ in range(girls+1) ]
    dp[0][0] = 1

    for g in range(girls+1):
        for b in range(boys+1):
            if g != b and boys-b != girls-g:
                dp[g][b] += dp[g-1][b] if g >= 1 else 0
                dp[g][b] += dp[g][b-1] if b >= 1 else 0

    return dp[girls-1][boys] + dp[girls][boys-1]

ans = solve()
print(ans)


def solve1(girls, boys):
    dp = [ [0 for _ in range(boys+1)] for _ in range(girls+1) ]
    dp[0][0] = 1

    for g in range(girls+1):
        for b in range(boys+1):
            if g != b and boys-b != girls-g:
                dp[g][b] += dp[g-1][b] if g >= 1 else 0
                dp[g][b] += dp[g][b-1] if b >= 1 else 0

    return dp[girls-1][boys] + dp[girls][boys-1]

ans = solve1(10, 20)
print(ans)

ans = solve1(20, 10)
print(ans)

ans = solve1(3, 3)
print(ans)
