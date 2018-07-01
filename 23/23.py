import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper


def solve1(round, coin):
    if coin == 0:
        return 0

    if round == 0:
        return 1

    win = solve1(round-1, coin+1)
    lost = solve1(round-1, coin-1)
    return win+lost

@timethis
def test1():
    print(solve1(24, 10))



def solve2(d, round, coin):
    if (round, coin) in d:
        return d[(round, coin)]

    if coin == 0:
        return 0

    if round == 0:
        return 1

    d[(round, coin)] = solve2(d, round-1, coin-1) + solve2(d, round-1, coin+1)
    return d[(round, coin)]

@timethis
def test2():
    d = {}
    print(solve2(d, 24, 10))


test1()
test2()
