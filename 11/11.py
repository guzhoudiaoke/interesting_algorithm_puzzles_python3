import time

def fib1(n):
    if n == 0 or n == 1:
        return 1
    return fib1(n-1) + fib1(n-2)

def solve1(n):
    ans = []
    j = 0
    while len(ans) < n:
        while True:
            f = fib1(j)
            j += 1
            s = sum(int(x) for x in str(f))
            if f % s == 0:
                ans += [f]
                break
    return ans


start_time = time.perf_counter()
ans = solve1(7)
print(ans)
end_time = time.perf_counter()
print('time cost: ', end_time - start_time)



def fib2(d, n):
    if n in d:
        return d[n]

    if n == 0 or n == 1:
        d[n] = 1
    else:
        d[n] = fib2(d, n-1) + fib2(d, n-2)

    return d[n]

def solve2(n):
    d = {}
    ans = []
    j = 0
    while len(ans) < n:
        while True:
            f = fib2(d, j)
            j += 1
            s = sum(int(x) for x in str(f))
            if f % s == 0:
                ans += [f]
                break
    return ans


start_time = time.perf_counter()
ans = solve2(17)
print(ans)
end_time = time.perf_counter()
print('time cost: ', end_time - start_time)


def solve3(n):
    ans = [1, 1]
    a, b = 1, 1
    while len(ans) < n:
        f = a + b
        s = sum(int(x) for x in str(f))
        if f % s == 0:
            ans += [f]
        a, b = b, f
    return ans


start_time = time.perf_counter()
ans = solve3(17)
print(ans)
end_time = time.perf_counter()
print('time cost: ', end_time - start_time)
