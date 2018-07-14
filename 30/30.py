import time
import itertools
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, 'cost time:', end - start)
        return result
    return wrapper


@timethis
def solve1(n):
    def dfs(n):
        if n == 1:
            return 1

        cnt = 0
        for i in range(1, n//2 + 1):
            if n == i*2:
                solve_i = dfs(i)
                cnt += solve_i * (solve_i + 1) // 2
            else:
                cnt += dfs(i) * dfs(n-i)

        for i in range(1, n//3 + 1):
            for j in range(i, (n-i) // 2 + 1):
                if i == j and i == (n - i - j):
                    solve_i = dfs(i)
                    cnt += solve_i * (solve_i + 1) * (solve_i + 2) // 6
                elif i == j:
                    solve_i = dfs(i)
                    cnt += solve_i * (solve_i + 1) // 2 * dfs(n - i*2)
                elif i == (n - i - j):
                    solve_i = dfs(i)
                    cnt += solve_i * (solve_i + 1) // 2 * dfs(n - i*2)
                elif j == (n - i - j):
                    solve_j = dfs(j)
                    cnt += solve_j * (solve_j + 1) // 2 * dfs(n - j*2)
                else:
                    cnt += dfs(i) * dfs(j) * dfs(n - i - j)

        return cnt

    return dfs(n)


@timethis
def solve2(n):
    def dfs(n):
        if n == 1:
            return 1

        if n in memo:
            return memo[n]

        cnt = 0
        for i in range(1, n//2 + 1):
            if (n - i) == i:
                solve_i = dfs(i)
                cnt += solve_i * (solve_i + 1) // 2
            else:
                cnt += dfs(i) * dfs(n-i)

        for i in range(1, n//3 + 1):
            for j in range(i, (n-i) // 2 + 1):
                if i == j and i == (n - i - j):
                    solve_i = dfs(i)
                    cnt += solve_i * (solve_i + 1) * (solve_i + 2) // 6
                elif i == j:
                    solve_i = dfs(i)
                    cnt += solve_i * (solve_i + 1) // 2 * dfs(n - i*2)
                elif i == (n - i - j):
                    solve_i = dfs(i)
                    cnt += solve_i * (solve_i + 1) // 2 * dfs(n - i*2)
                elif j == (n - i - j):
                    solve_j = dfs(j)
                    cnt += solve_j * (solve_j + 1) // 2 * dfs(n - j*2)
                else:
                    cnt += dfs(i) * dfs(j) * dfs(n - i - j)

        memo[n] = cnt
        return cnt

    memo = {}
    return dfs(n)

print(solve1(20))
print(solve2(20))
