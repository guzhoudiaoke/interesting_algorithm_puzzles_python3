num = 11
while True:
    s10 = str(num)
    s2  = str(bin(num))[2:]
    s8  = str(oct(num))[2:]
    if s10 == s10[::-1] and s2 == s2[::-1] and s8 == s8[::-1]:
        break
    num += 2

print(num, bin(num), oct(num))

num = 11
while True:
    s10 = str(num)
    s2  = format(num, 'b')
    s8  = format(num, 'o')
    if s10 == s10[::-1] and s2 == s2[::-1] and s8 == s8[::-1]:
        break
    num += 2

print(num, bin(num), oct(num))
