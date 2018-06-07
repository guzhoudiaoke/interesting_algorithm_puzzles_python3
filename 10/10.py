def max_sum(nums, n):
    s = ans = sum(nums[:n])
    length = len(nums)
    for i in range(length):
        s += nums[(i+n) % length] - nums[i]
        ans = max(ans, s)
    return ans

def solve():
    european = [
            0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 
            11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 
            22, 18, 29, 7, 28, 12, 35, 3, 26 ]
    american = [
            0, 28, 9, 26, 30, 11, 7, 20, 32, 17, 5, 22, 34, 15, 
            3, 24, 36, 13, 1, 0, 27, 10, 25, 29, 12, 8, 19, 31, 
            18, 6, 21, 33, 16, 4, 23, 35, 14, 2 ]

    ans = []
    for i in range(2, 37):
        if max_sum(european, i) < max_sum(american, i):
            ans += [i]
    return ans

ans = solve()
print(ans)
print(len(ans))
