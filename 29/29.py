import itertools
from fractions import Fraction

def product(cand):
    def dfs(cand, i, length, current, result):
        if i == length:
            result.append(current)
        else:
            for x in cand[i]:
                dfs(cand, i+1, length, current + [x], result)

    result = []
    dfs(cand, 0, len(cand), [], result)
    return result


def parallel(arr):
    s = sum([Fraction(1, x) for x in arr])
    return Fraction(1, s)


def solve(n):
    def dfs(n):
        if n in memo:
            return memo[n]

        # series connection
        result = [x + 1 for x in dfs(n-1)]

        # parallel connection
        nums = [ i for i in range(1, n) ]
        for i in range(2, n):
            cuts = {}
            for comb in itertools.combinations(nums, i-1):
                r = sorted([comb[0]] + [ comb[i] - comb[i-1] for i in range(1, len(comb)) ] + [n - comb[-1]])
                cuts[str(r)] = r

            keys = [ [dfs(c) for c in v] for k, v in cuts.items() ]
            for k in keys:
                conns = product(k)
                for c in conns:
                    result.append(parallel(c))

        memo[n] = result
        return result

    memo = {1 : [1]}
    golden = 1.61800339887
    ans = float('INF')

    cands = dfs(n)
    for c in cands:
        if abs(golden - c) < abs(golden - ans):
            ans = c

    return ans


def test():
    result = solve(10)
    print(result, float(result))

test()
