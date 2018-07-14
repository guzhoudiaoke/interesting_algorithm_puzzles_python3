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


def solve1(clubs, n):
    ans = 0
    for i in range(1, len(clubs)+1):
        for comb in itertools.combinations(clubs, i):
            size, student = 0, 0
            for c in comb:
                size += c[0]
                student += c[1]
                if student > n:
                    break

            if student <= n and size > ans:
                ans = size
    return ans


def solve2(clubs, n):
    memo = {}
    visited = [0] * len(clubs)

    def dfs(left):
        key = str((visited, left))
        if key in memo:
            return memo[key]

        m = 0
        for i in range(len(clubs)):
            if visited[i] == 0:
                visited[i] = 1
                if left >= clubs[i][1]:
                    m = max(m, clubs[i][0] + dfs(left - clubs[i][1]))
                visited[i] = 0

        memo[key] = m
        return m

    return dfs(n)


def solve3(clubs, n):
    memo = {}

    def dfs(clubs, left):
        key = str((clubs, left))
        if key in memo:
            return memo[key]

        m = 0
        for c in clubs:
            if left >= c[1]:
                m = max(m, c[0] + dfs(clubs - {c}, left - c[1]))

        memo[key] = m
        return m

    return dfs(clubs, n)


def solve4(clubs, n):
    dp = [ [0 for j in range(n+1) ] for i in range(len(clubs)+1) ]
    for i in range(len(clubs)-1, -1, -1):
        for j in range(n+1):
            if j < clubs[i][1]:
                dp[i][j] = dp[i+1][j]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i+1][j-clubs[i][1]] + clubs[i][0])

    return dp[0][n]


@timethis
def test1():
    clubs = [ (11000, 40), (8000, 30), (400, 24), (800, 20), (900, 14),
              (1800, 16), (1000, 15), (7000, 40), (100, 10), (300, 12) ]
    ans = solve1(clubs, 150)
    print(ans)

test1()


@timethis
def test2():
    clubs = [ (11000, 40), (8000, 30), (400, 24), (800, 20), (900, 14),
              (1800, 16), (1000, 15), (7000, 40), (100, 10), (300, 12) ]
    ans = solve2(clubs, 150)
    print(ans)

test2()


@timethis
def test3():
    clubs = { (11000, 40), (8000, 30), (400, 24), (800, 20), (900, 14),
              (1800, 16), (1000, 15), (7000, 40), (100, 10), (300, 12) }
    ans = solve3(clubs, 150)
    print(ans)

test3()


@timethis
def test4():
    clubs = [ (11000, 40), (8000, 30), (400, 24), (800, 20), (900, 14),
              (1800, 16), (1000, 15), (7000, 40), (100, 10), (300, 12) ]
    ans = solve4(clubs, 150)
    print(ans)

test4()
