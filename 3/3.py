def solve(n):
    cards = [False] * n
    for i in range(2, n+1):
        for j in range(i-1, n, i):
            cards[j]  = not cards[j]

    ans = []
    for i in range(n):
        if not cards[i]:
            ans.append(i+1)

    return ans


def solve2(n):
    if n < 1:
        return []

    ans = [1]
    for i in range(2, n+1):
        flag = False
        for j in range(2, i):
            if i % j == 0:
                flag = not flag

        if flag:
            ans.append(i)

    return ans

def solve3(n):
    ans = []
    i = 1
    while i*i <= n:
        ans.append(i*i)
        i += 1

    return ans

ans = solve(100)
print(ans)

ans = solve2(100)
print(ans)

ans = solve3(100)
print(ans)
