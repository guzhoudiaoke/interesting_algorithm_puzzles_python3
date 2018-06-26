from itertools import combinations
import time
import math

def solve1(n):
    ans = set()
    for c in range(1, n // 4 + 1):
        s = c * c
        for a in range(1, c):
            sa = a * (2*c - a)
            for b in range(1, a):
                sb = b * (2*c - b)
                if s == sa + sb:
                    ans |= {1.0 * sb / sa}
    return ans

s = time.perf_counter()
ans = solve1(2000)
e = time.perf_counter()
print(ans)
print(len(ans))
print('time cost', e - s)


def solve2(n):
    ans = set()
    for c in range(1, n // 4 + 1):
        s = c * c
        cands = [ i * (2*c - i) for i in range(1, c) ]
        for sa, sb in combinations(cands, 2):
            if sa + sb == s:
                ans |= {1.0 * sa / sb}
    return ans

s = time.perf_counter()
ans = solve2(2000)
e = time.perf_counter()
print(ans)
print(len(ans))
print('time cost', e - s)



def solve3(n):
    ans = set()
    for c in range(1, n // 4 + 1):
        s = c * c
        cands = [ i for i in range(1, c) ]
        for a, b in combinations(cands, 2):
            sa, sb = a*a, b*b
            if sa + sb == s:
                ans |= {1.0 * sa / sb}
    return ans

s = time.perf_counter()
ans = solve3(2000)
e = time.perf_counter()
print(ans)
print(len(ans))
print('time cost', e - s)




def solve4(n):
    ans = []
    for c in range(1, n // 4 + 1):
        s = c * c
        cands = [ i for i in range(1, c) ]
        for a, b in combinations(cands, 2):
            if a*a + b*b == s:
                if math.gcd(a, b) == 1:
                    ans.append((a, b, c))
    return ans

s = time.perf_counter()
ans = solve4(2000)
e = time.perf_counter()
print(ans)
print(len(ans))
print('time cost', e - s)




def solve5(n):
    ans = []
    squars = { i*i : i for i in range(n//4 + 1) }
    for c in range(1, n // 4 + 1):
        s = c * c
        for a in range(1, c):
            sa = a*a
            sb = s - sa
            if sb in squars and sb < sa:
                b = squars[s - a*a]
                if math.gcd(a, b) == 1:
                    ans.append((a, b, c))
    return ans

s = time.perf_counter()
ans = solve5(2000)
e = time.perf_counter()
print(ans)
print(len(ans))
print('time cost', e - s)

