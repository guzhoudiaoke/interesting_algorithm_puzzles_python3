countries = ["Algeria", "Argentina", "Australia", "Belgium", "Bosnia and Herzegovina", 
             "Brazil", "Cameroon", "Chile", "Colombia", "Costa Rica", "Croatia", "Ecuador", 
             "England", "France", "Germany", "Ghana", "Greece", "Honduras", "Iran", "Italy", 
             "Cote d'Ivoire", "Japan", "Mexico", "Netherlands", "Nigeria", "Portugal", "Russia", 
             "Korea Republic", "Spain", "Switzerland", "USA", "Uruguay"]

def solve(countries):
    def dfs(prev_country, depth):
        if ans[0] < depth:
            ans[0] = depth

        for i, c in enumerate(countries):
            if not used[i] and c[0].lower() == prev_country[-1].lower():
                used[i] = True
                dfs(c, depth+1)
                used[i] = False

    ans = [0]
    used = [False] * len(countries)
    for i, c in enumerate(countries):
        used[i] = True
        dfs(c, 1)
        used[i] = False

    return ans[0]

print(solve(countries))


import copy
class Solution():
    def solve(self, countries):
        def dfs(current):
            if len(self.ans) < len(current):
                self.ans = copy.deepcopy(current)

            for i, c in enumerate(countries):
                if not used[i] and c[0].lower() == current[-1][-1].lower():
                    used[i] = True
                    dfs(current+[c])
                    used[i] = False

        self.ans = []
        used = [False] * len(countries)
        for i, c in enumerate(countries):
            used[i] = True
            dfs([c])
            used[i] = False

        return self.ans

sol = Solution()
print(sol.solve(countries))




import copy
def solve1(countries):
    def dfs(current):
        global ans
        if len(ans) < len(current):
            ans = copy.deepcopy(current)

        for i, c in enumerate(countries):
            if not used[i] and c[0].lower() == current[-1][-1].lower():
                used[i] = True
                dfs(current+[c])
                used[i] = False

    used = [False] * len(countries)
    for i, c in enumerate(countries):
        used[i] = True
        dfs([c])
        used[i] = False

ans = []
solve1(countries)
print(ans)
print(len(ans))



b = 12
def get():
    global b
    b = b + 2
    return b

print(get())

l = [1, 2]
def getlist():
    global l
    l = [1, 2, 3]
    return l

print(getlist())

def test():
    global ll
    ll = [1, 2, 3, 4]
    return ll

ll = [1]
print(test())

