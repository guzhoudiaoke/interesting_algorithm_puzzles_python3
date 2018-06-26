import time

def solve1(n, current):
    if len(current) == n:
        return 1

    ans = solve1(n, current + 'B')
    if len(current) == 0 or current[-1] == 'B':
        ans += solve1(n, current + 'G')

    return ans

s = time.perf_counter()
ans = solve1(30, '')
e = time.perf_counter()
print(ans)
print('time cost: ', e-s)


def solve2(n, current):
    if len(current) == n:
        return 1

    ans = solve1(n, current + 'B')
    if current[-1] == 'B':
        ans += solve1(n, current + 'G')

    return ans

s = time.perf_counter()
ans = solve2(30, 'B') + solve2(30, 'G')
e = time.perf_counter()
print(ans)
print('time cost: ', e-s)




def solve3(n, last):
    if n == 0:
        return 1

    if last == 'B':
        return solve3(n-1, 'B') + solve3(n-1, 'G')
    else:
        return solve3(n-1, 'B')


s = time.perf_counter()
ans = solve3(29, 'B') + solve3(29, 'G')
e = time.perf_counter()
print(ans)
print('time cost: ', e-s)



def solve4(n, d):
    if n == 1 or n == 2:
        return n+1

    if n in d:
        return d[n]

    d[n] = solve4(n-1, d) + solve4(n-2, d)
    return d[n]

s = time.perf_counter()
d = {}
ans = solve4(30, d)
e = time.perf_counter()
print(ans)
print('time cost: ', e-s)




for i in range(10):
    print(solve1(i, ''), end=', ')
print()

def solve5(n):
    b, g = 1, 0
    for i in range(n):
        b, g = b + g, b
    return b + g

s = time.perf_counter()
ans = solve5(30)
e = time.perf_counter()
print(ans)
print('time cost: ', e-s)
