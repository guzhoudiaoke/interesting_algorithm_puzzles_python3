import time
import copy


def solve1(total, prev, used, squares):
    if total == len(used):
        if prev+1 in squares:
            return True
    else:
        for i in range(2, total+1):
            if (i+prev) in squares and i not in used:
                if solve1(total, i, used+[i], squares):
                    return True
    return False

def test1():
    start = time.perf_counter()
    n = 2
    while True:
        squares = { i*i for i in range(2, int(n ** 2)) }
        if solve1(n, 1, [1], squares):
            print(n)
            break
        n += 1
    end = time.perf_counter()
    print('solve1 time cost: ', end - start)





def solve2(total, left, prev, used, squares):
    if left == 0:
        if prev+1 in squares:
            return True
    else:
        for i in range(2, total+1):
            if not used[i] and (i+prev) in squares:
                used[i] = True
                if solve2(total, left-1, i, used, squares):
                    return True
                used[i] = False
    return False


def test2():
    start = time.perf_counter()
    n = 2
    while True:
        squares = { i*i for i in range(2, int(n ** 2)) }
        used = [False] * (n+1)
        used[1] = True
        if solve2(n, n-1, 1, used, squares):
            print(n)
            break
        n += 1
    end = time.perf_counter()
    print('solve2 time cost: ', end - start)




def solve3(total, prev, used, squares):
    if total == len(used):
        if prev+1 in squares:
            print(used)
            return True
    else:
        for i in range(2, total+1):
            if (i+prev) in squares and i not in used:
                if solve3(total, i, used+[i], squares):
                    return True
    return False

def test3():
    start = time.perf_counter()
    n = 2
    while True:
        squares = { i*i for i in range(2, int(n ** 2)) }
        ans = solve3(n, 1, [1], squares)
        if ans:
            print(ans)
            break
        n += 1
    end = time.perf_counter()
    print('solve1 time cost: ', end - start)




seq = []
def solve4(total, left, prev, used, squares):
    if left == 0:
        if prev+1 in squares:
            return True
    else:
        for i in range(2, total+1):
            if not used[i] and (i+prev) in squares:
                used[i] = True
                seq.append(i)
                if solve4(total, left-1, i, used, squares):
                    return True
                used[i] = False
                seq.pop()
    return False


def test4():
    start = time.perf_counter()
    n = 2
    while True:
        squares = { i*i for i in range(2, int(n ** 2)) }
        used = [False] * (n+1)
        used[1] = True
        global seq
        seq = [1]
        if solve4(n, n-1, 1, used, squares):
            print(n)
            break
        n += 1
    end = time.perf_counter()
    print(seq)
    print('solve2 time cost: ', end - start)



test1()
test2()
test3()
test4()

