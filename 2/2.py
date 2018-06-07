ops = ['+', '-', '*', '/', '']

def solve2():
    for i in range(10, 100):
        s = str(i)
        for op1 in ops:
            exp = s[0] + op1 + s[1]
            if len(exp) > len(s):
                try:
                    if s[::-1] == str(eval(exp)):
                        ans.append(exp + '=' + s[::-1])
                except:
                    pass

ans = []
solve2()
print(ans)

def solve3():
    for i in range(100, 1000):
        s = str(i)
        for op1 in ops:
            for op2 in ops:
                exp = s[0] + op1 + s[1] + op2 + s[2]
                if len(exp) > len(s):
                    try:
                        if s[::-1] == str(eval(exp)):
                            ans.append(exp + '=' + s[::-1])
                    except:
                        pass

ans = []
solve3()
print(ans)

def solve4():
    for i in range(1000, 10000):
        s = str(i)
        for op1 in ops:
            for op2 in ops:
                for op3 in ops:
                    exp = s[0] + op1 + s[1] + op2 + s[2] + op3 + s[3]
                    if len(exp) > len(s):
                        try:
                            if s[::-1] == str(eval(exp)):
                                ans.append(exp + '=' + s[::-1])
                        except:
                            pass

ans = []
solve4()
print(ans)

def dfs(num, pos, exp):
    s = str(num)
    if pos == len(s):
        if len(exp) > len(s):
            try:
                if s[::-1] == str(eval(exp)):
                    ans.append(exp + '=' + s[::-1])
            except:
                pass
        return

    for op in ops:
        dfs(s, pos+1, exp+op+s[pos])

ans = []
for i in range(10, 6000):
    if dfs(i, 1, str(i)[0]):
        ans.append(i)
print(ans)


def dfs2(num, pos, exp):
    s = str(num)
    if pos == len(s)-1:
        if len(exp) >= len(s):
            exp = exp + s[-1]
            try:
                if s[::-1] == str(eval(exp)):
                    ans.append(exp + '=' + s[::-1])
            except:
                pass
        return

    for op in ops:
        dfs2(s, pos+1, exp+s[pos]+op)

ans = []
for i in range(10, 6000):
    if dfs2(i, 0, ''):
        ans.append(i)
print(ans)

