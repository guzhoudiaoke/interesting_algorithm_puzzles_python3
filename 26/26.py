import collections

def solve1(width, height):
    def in_board(r, c):
        return r >= 0 and c >= 0 and r < height and c < width

    q = collections.deque()
    q.append((0, 0, height-1, width-1))

    log = {}
    log[(0, 0, height-1, width-1)] = 0

    while q:
        car_r, car_c, space_r, space_c = q.popleft()
        depth = log[(car_r, car_c, space_r, space_c)]

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            sr, sc = space_r + dr, space_c + dc
            if not in_board(sr, sc):
                continue

            cr, cc = car_r, car_c
            if car_r == sr and car_c == sc:
                cr, cc = space_r, space_c
                if cr == height-1 and cc == width-1:
                    return depth+1

            if (cr, cc, sr, sc) not in log:
                log[(cr, cc, sr, sc)] = depth+1
                q.append((cr, cc, sr, sc))

ans = solve1(2, 3)
print(ans)

ans = solve1(10, 10)
print(ans)



def solve2(width, height):
    def in_board(r, c):
        return r >= 0 and c >= 0 and r < height and c < width

    def get_path(start):
        path = []
        while start:
            path.insert(0, start)
            start = log[start][1]
        return path

    q = collections.deque()
    q.append((0, 0, height-1, width-1))

    log = {}
    log[(0, 0, height-1, width-1)] = [0, None]

    while q:
        car_r, car_c, space_r, space_c = q.popleft()
        depth = log[(car_r, car_c, space_r, space_c)][0]

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            sr, sc = space_r + dr, space_c + dc
            if not in_board(sr, sc):
                continue

            cr, cc = car_r, car_c
            if car_r == sr and car_c == sc:
                cr, cc = space_r, space_c
                if cr == height-1 and cc == width-1:
                    path = get_path((car_r, car_c, space_r, space_c))
                    path.append((cr, cc, sr, sc))
                    return depth+1, path

            st = (cr, cc, sr, sc)
            if st not in log:
                log[st] = [depth+1, (car_r, car_c, space_r, space_c)]
                q.append(st)

ans = solve2(3, 2)
print(ans)

ans = solve2(10, 10)
print(ans)
