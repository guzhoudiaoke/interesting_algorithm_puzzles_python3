def solve(n):
    x = n*3 + 1
    while True:
        x = x // 2 if x % 2 == 0 else x*3 + 1
        if x == 1:
            return False
        if x == n:
            return True
    return False

cnt = 0
for i in range(0, 10001, 2):
    if solve(i):
        cnt += 1
print(cnt)
