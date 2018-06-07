from itertools import permutations
import time

def solve1():
    ans = []
    for r, e, a, d, w, i, t, l, k, s in permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
        if r == 0 or w == 0 or t == 0 or s == 0:
            continue
        read  = r*1000  + e*100  + a*10  + d
        write = w*10000 + r*1000 + i*100 + t*10 + e
        talk  = t*1000  + a*100  + l*10  + k
        skill = s*10000 + k*1000 + i*100 + l*10 + l

        if read + write + talk == skill:
            ans += [(read, write, talk, skill)]
    return ans

start = time.perf_counter()
ans = solve1()
end = time.perf_counter()
for a in ans:
    print(a[0], "+", a[1], "+", a[2], "=", a[3])
print("cost time: ", end-start)



def solve2():
    ans = []

    for r, e, a, d, w, i, t, l, k, s in permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
        if r == '0' or w == '0' or t == '0' or s == '0':
            continue
        read  = r + e + a + d
        write = w + r + i + t + e
        talk  = t + a + l + k
        skill = s + k + i + l + l
        exp = read + "+" + write + "+" + talk + "==" + skill
        if eval(exp):
            ans += exp,

    return ans

start = time.perf_counter()
ans = solve2()
end = time.perf_counter()
for a in ans:
    print(a)
print("cost time: ", end-start)


import re
def solve3(expression):
    nums = [ n for n in re.split(r'\W', expression) if len(n) > 0 ]
    print(nums)
    chars = ''.join(list(set(''.join(nums))))
    print(chars)
    heads = set([ w[0] for w in nums ])
    print(heads)

    ans = []
    all_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for perm in permutations(all_num, len(chars)):
        seq = ''.join(perm)
        index = seq.find('0')
        if index >= 0 and chars[index] in heads:
            continue

        trans_table = str.maketrans(chars, seq)
        e = expression.translate(trans_table)
        if eval(e):
            ans.append(e)

    return ans

start = time.perf_counter()
expression = "READ+WRITE+TALK==SKILL"
ans = solve3(expression)
end = time.perf_counter()
for a in ans:
    print(a)
print("cost time: ", end-start)



def solve4():
    ans = []
    all_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    num_set = set(all_nums)
    for e, a, d, t, l, k in permutations(all_nums, 6):
        if (a+t == 8 or a+t == 9 or a+t == 10) and \
           (a+e == 8 or a+e == 9 or a+e == 10) and \
           ((d+e+k) % 10 == l) and \
           (((a+t+l) * 10 + d + e + k) % 100 == l*11):
                for i, r, s, w in permutations(list(num_set - {k, e, d, l, t, a}), 4):
                    if r == 0 or w == 0 or t == 0 or s == 0:
                        continue

                    if r != 0 and w != 0 and t != 0 and s != 0 and \
                        (s == w+1 or s == w+2):
                            read  = r*1000  + e*100  + a*10  + d
                            write = w*10000 + r*1000 + i*100 + t*10 + e
                            talk  = t*1000  + a*100  + l*10  + k
                            skill = s*10000 + k*1000 + i*100 + l*10 + l

                            if read + write + talk == skill:
                                ans += [(read, write, talk, skill)]
    return ans

start = time.perf_counter()
ans = solve4()
end = time.perf_counter()
for a in ans:
    print(a[0], "+", a[1], "+", a[2], "=", a[3])
print("cost time: ", end-start)
