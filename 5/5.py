def solve1(n):
    ans = 0
    for c500 in range(0, n//500 + 1):
        for c100 in range(0, n//100 + 1):
            for c50 in range(0, n//50 + 1):
                for c10 in range(0, n//10 + 1):
                    if c500 + c100 + c50 + c10 <= 15:
                        if 500*c500 + 100*c100 + 50*c50 + 10*c10 == n:
                            ans += 1
    return ans

print(solve1(1000))


import itertools
def solve2(n):
    coins = [500, 100, 50, 10]
    ans = 0
    for i in range(2, 16):
        for comb in itertools.combinations_with_replacement(coins, i):
            if sum(comb) == n:
                ans += 1
    return ans

print(solve2(1000))


def solve3(target, coins, max_num):
    def dfs(target, index, left):
        if index == len(coins):
            if target == 0:
                ans[0] += 1
        else:
            for i in range(0, target // coins[index] + 1):
                if i <= left:
                    dfs(target - coins[index]*i, index+1, left-i)

    ans = [0]
    dfs(target, 0, max_num)
    return ans[0]

print(solve3(1000, [500, 100, 50, 10], 15))
