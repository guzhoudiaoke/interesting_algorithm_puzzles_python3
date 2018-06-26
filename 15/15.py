import time

def solve1(step, a, b):
    if a > b:
        return 0
    if a == b:
        return 1

    cnt = 0
    for i in range(1, step+1):
        for j in range(1, step+1):
            cnt += solve1(step, a+i, b-j)
    return cnt

s = time.perf_counter()
ans = solve1(4, 0, 20)
e = time.perf_counter()
print(ans)
print("time: ", e-s)


def solve2(d, step, a, b):
    if (a, b) in d:
        return d[(a, b)]

    if a > b:
        d[(a, b)] = 0
    elif a == b:
        d[(a, b)] = 1
    else:
        cnt = 0
        for i in range(1, step+1):
            for j in range(1, step+1):
                cnt += solve2(d, step, a+i, b-j)
        d[(a, b)] = cnt

    return d[(a, b)]


s = time.perf_counter()
d = {}
ans = solve2(d, 4, 0, 200)
e = time.perf_counter()
print(ans)
print("time: ", e-s)


def solve3(step, a, b):
    dp = [0] * (b+1)
    dp[b] = 1

    ans = 0
    for i in range(b):
        for j in range(b+1):
            for k in range(1, step+1):
                if k <= j:
                    dp[j-k] += dp[j]
            dp[j] = 0
        if i % 2 == 1:
            ans += dp[0]
    return ans

s = time.perf_counter()
d = {}
ans = solve3(4, 0, 200)
e = time.perf_counter()
print(ans)
print("time: ", e-s)



def solve4(step, a, b):
    dp = [0] * (b+1)
    dp[0] = 1

    ans = 0
    for i in range(b):
        for j in range(b, -1, -1):
            for k in range(1, step+1):
                if k + j <= b:
                    dp[j+k] += dp[j]
            dp[j] = 0
        if i % 2 == 1:
            ans += dp[b]
    return ans

s = time.perf_counter()
d = {}
ans = solve4(4, 0, 200)
e = time.perf_counter()
print(ans)
print("time: ", e-s)



def solve5(step, a, b):
    dp = [[0] * (b+1) for i in range(b+1)]
    dp[0][0] = 1

    for i in range(b):
        for j in range(b+1):
            for k in range(1, step+1):
                if j + k <= b:
                    dp[i+1][j+k] += dp[i][j]

    ans = 0
    for i in range(0, b+1, 2):
        ans += dp[i][b]

    return ans

s = time.perf_counter()
d = {}
ans = solve5(4, 0, 200)
e = time.perf_counter()
print(ans)
print("time: ", e-s)


