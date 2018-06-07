import time

n = 15

def solve1(log, n):
    if len(log) == n+1:
        return 1

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    count = 0
    for d in directions:
        next = log[-1][0] + d[0], log[-1][1] + d[1]
        if next not in log:
            count += solve1(log + [next], n)
    return count



start_time = time.clock()
ans = solve1([(0, 0)], n)
end_time = time.clock()
print('solve1: ', ans, 'time cost: ', end_time - start_time)


def solve2(graph, pos, left):
    if left == 0:
        return 1

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    count = 0
    for d in directions:
        next = pos[0] + d[0], pos[1] + d[1]
        if graph[next[0]][next[1]] == 0:
            graph[next[0]][next[1]] = 1
            count += solve2(graph, next, left-1)
            graph[next[0]][next[1]] = 0
    return count

start_time = time.clock()
graph = [[0] * n*2 for j in range(0, n*2)]
graph[0][0] = 1
ans = solve2(graph, (0, 0), n)
end_time = time.clock()
print('solve2: ', ans, 'time cost: ', end_time - start_time)



#➜  8 python 8.py
#solve1:  881500 time cost:  1.24
#solve2:  881500 time cost:  0.76
#➜  8 python 8.py
#solve1:  2374444 time cost:  3.45
#solve2:  2374444 time cost:  2.0300000000000002
#➜  8 python 8.py
#solve1:  6416596 time cost:  9.57
#solve2:  6416596 time cost:  5.5
