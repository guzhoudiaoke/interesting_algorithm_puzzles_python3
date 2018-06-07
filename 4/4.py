def solve1(n, m, current):
    if current >= n:
        return 0
    if current <= m:
        return 1 + solve1(n, m, current*2)
    else:
        return 1 + solve1(n, m, current + m)

print(solve1(20, 3, 1))
print(solve1(100, 5, 1))

def solve2(n, m):
    ans, current = 0, 1
    while current < n:
        current += current if current < m else m
        ans += 1
    return ans

print(solve2(20, 3))
print(solve2(100, 5))
