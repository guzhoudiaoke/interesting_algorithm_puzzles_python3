from itertools import permutations

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def solve(n):
    primes = []
    x = 2
    while len(primes) < n:
        if is_prime(x):
            primes += [x]
        x += 1

    ans = (primes[-1] * primes[-1], [])
    for perm in permutations(primes):
        friends = [perm[0] * perm[0], perm[-1] * perm[-1]] + [perm[i]*perm[i-1] for i in range(1, len(perm))]
        if max(friends) < ans[0]:
            ans = max(friends), friends
    return ans

ans = solve(6)
print(ans)
