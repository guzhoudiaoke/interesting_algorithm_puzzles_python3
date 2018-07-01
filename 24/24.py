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


def solve1(d, board):
    if str(board) in d:
        return d[str(board)]

    count = 0
    for i in board:
        new_board = []
        for j in board:
            if len(i & j) == 0:
                new_board.append(j)
        count += solve1(d, new_board)

    d[str(board)] = count
    return count

@timethis
def test1():
    board = [ {1, 2}, {2, 3}, {7, 8}, {8, 9}, {1, 4}, {4, 7}, {3, 6}, {6, 9} ]
    for i in range(1, 10):
        board.append({i})

    d = {}
    d[str([])] = 1
    ans = solve1(d, board)
    print(ans)

test1()



def solve2(d, board):
    if str(board) in d:
        return d[str(board)]

    count = 0
    for i in board:
        count += solve2(d, [j for j in board if len(i & j) == 0])

    d[str(board)] = count
    return count

@timethis
def test2():
    board = [ {1, 2}, {2, 3}, {7, 8}, {8, 9}, {1, 4}, {4, 7}, {3, 6}, {6, 9} ]
    for i in range(1, 10):
        board.append({i})

    d = {}
    d[str([])] = 1
    ans = solve2(d, board)
    print(ans)


test2()
