def solve1(n):
    count, ans = 0, 1
    row = [1]

    while count < n:
        next_row = [1]
        for i in range(len(row) - 1):
            x = row[i] ^ row[i+1]
            next_row.append(x)
            if x == 0:
                count += 1

        next_row.append(1)
        ans += 1
        row = next_row
    
    return ans

print(solve1(2018))



def solve2(n):
    count, ans, row = 0, 1, 1

    while count < n:
        row ^= (row << 1)
        count += format(row, 'b').count("0")
        ans += 1
    
    return ans

print(solve2(2018))
