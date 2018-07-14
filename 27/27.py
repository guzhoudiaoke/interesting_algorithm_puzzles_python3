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

@timethis
def solve1(width, height):
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    rows = [ [False for i in range(width)] for j in range(height+1) ]
    cols = [ [False for i in range(height)] for j in range(width+1) ]

    def dfs(direction, r, c):
        rr, cc = r, c
        if direction == 0 or direction == 2: # forward or backward
            rr = r + directions[direction][1]
            if rr < 0 or rr > height:
                return 0
            if cols[c][min(r, rr)]:
                return 0
        else:
            cc = c + directions[direction][0]
            if cc < 0 or cc > width:
                return 0
            if rows[r][min(c, cc)]:
                return 0

        next_row, next_col = r + directions[direction][1], c + directions[direction][0]
        if next_row < 0 or next_row > height or next_col < 0 or next_col > width:
            return 0

        if next_row == height and next_col == width:
            return 1

        if direction == 0 or direction == 2:
            cols[c][min(r, rr)] = True
        else:
            rows[r][min(c, cc)] = True

        count = 0
        count += dfs(direction, next_row, next_col)
        count += dfs((direction + 1) % len(directions), next_row, next_col)

        if direction == 0 or direction == 2:
            cols[c][min(r, rr)] = False
        else:
            rows[r][min(c, cc)] = False

        return count

    return dfs(3, 0, 0)


ans = solve1(6, 4)
print(ans)



@timethis
def solve2(width, height):
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    rows = [ [False for i in range(width)] for j in range(height+1) ]
    cols = [ [False for i in range(height)] for j in range(width+1) ]

    def dfs(direction, r, c):
        next_row, next_col = r + directions[direction][1], c + directions[direction][0]

        # reach it
        if next_row == height and next_col == width:
            return 1

        # out of range
        if next_row < 0 or next_row > height or next_col < 0 or next_col > width:
            return 0

        rr, cc = r, c
        if direction == 0 or direction == 2: # forward or backward
            rr = min(r, next_row)
            if cols[c][rr]:
                return 0
            cols[c][rr] = True
        else:
            cc = min(c, next_col)
            if rows[r][cc]:
                return 0
            rows[r][cc] = True

        count = 0
        count += dfs(direction, next_row, next_col)
        count += dfs((direction + 1) % len(directions), next_row, next_col)

        if direction == 0 or direction == 2:
            cols[c][rr] = False
        else:
            rows[r][cc] = False

        return count

    return dfs(3, 0, 0)


ans = solve2(6, 4)
print(ans)
