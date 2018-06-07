n = 1
while True:
    s = format(n ** 0.5, '10.10f').split('.')
    ss = (s[0] + s[1])[: 10]
    if len(set(ss)) == 10:
        break

    n += 1
print(n, str(n ** 0.5)[:11])


n = 1
while True:
    s = format(n ** 0.5, '10.10f')
    i = s.index('.')
    s = s[:i] + s[i+1:11]
    if len(set(s)) == 10:
        break

    n += 1
print(n, str(n ** 0.5)[:11])


n = 1
while True:
    s = format(n ** 0.5, '10.10f')
    if len(set(s[:11])) == 11:
        break

    n += 1
print(n, str(n ** 0.5)[:11])


n = 1
while True:
    s = format(n ** 0.5, '10.10f').split('.')
    if len(set(s[1])) == 10:
        break

    n += 1

s = str(n ** 0.5)
i = s.index('.')
print(n, s[: i+11])



n = 1
while True:
    s = format(n ** 0.5, '10.10f')
    i = s.index('.')
    s = s[i+1 : i+11]
    if len(set(s)) == 10:
        break

    n += 1

s = str(n ** 0.5)
i = s.index('.')
print(n, s[: i+11])

