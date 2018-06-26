import itertools
import time

square = [1, 14, 14, 4, 11, 7, 6, 9,
          8, 10, 10, 5, 13, 2, 3, 15]

def solve1(square):
    d = {}
    for size in range(1, len(square)):
        combs = itertools.combinations(square, size)
        for t in combs:
            s = sum(t)
            if s in d:
                d[s] += 1
            else:
                d[s] = 1

    m = max(d, key=d.get)
    print(m, d[m])

s = time.perf_counter()
solve1(square)
e = time.perf_counter()
print("time cost: ", e-s)

def solve2(square):
    all = sum(square)
    dp = [0] * (all + 1)
    dp[0] = 1

    for n in square:
        for i in range(all - n, -1, -1):
            dp[i + n] += dp[i]

    m = max(dp)
    print(dp.index(m), m)

s = time.perf_counter()
solve2(square)
e = time.perf_counter()
print("time cost: ", e-s)
