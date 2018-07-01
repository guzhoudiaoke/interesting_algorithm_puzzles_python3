import time
import itertools
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, 'cost time:', end - start)
        return result
    return wrapper


def solve1(n):
    ans = 0
    nums = [i for i in range(1, n+1)]
    for perm_left in itertools.permutations(nums):
        for perm_right in itertools.permutations(nums):
            path = []
            l, r = 0, perm_right[0]
            for i in range(n-1):
                path.append((l, r))
                l = perm_left[i]
                path.append((l, r))
                r = perm_right[i+1]
            path.append((l, 0))

            length = len(path)
            count = 0
            for i in range(length):
                for j in range(i+1, length):
                    if (path[i][0] > path[j][0] and path[i][1] < path[j][1]) or \
                            (path[i][0] < path[j][0] and path[i][1] > path[j][1]):
                        count += 1

            if ans < count:
                ans = count
    return ans


@timethis
def test1():
    print(solve1(6))

test1()


def solve2(n):
    ans = 0
    nums = [i for i in range(1, n+1)]
    for perm_left in itertools.permutations(nums):
        for perm_right in itertools.permutations(nums):
            path = []
            l, r = 0, perm_right[0]
            for i in range(n-1):
                path.append((l, r))
                l = perm_left[i]
                path.append((l, r))
                r = perm_right[i+1]
            path.append((l, 0))
            
            length = len(path)
            count = 0
            for i in range(length):
                for j in range(i+1, length):
                    if (path[i][0] - path[j][0]) * (path[i][1] - path[j][1]) < 0:
                        count += 1

            if ans < count:
                ans = count
    return ans


@timethis
def test2():
    print(solve2(6))

test2()
