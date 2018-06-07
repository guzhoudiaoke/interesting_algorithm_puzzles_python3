from datetime import datetime, date, timedelta

def solve1(date_start, date_end):
    ans = []
    step = timedelta(days=1)
    d = datetime.strptime(date_start, '%Y-%m-%d').date()
    while d < datetime.strptime(date_end, '%Y-%m-%d').date():
        n = int(d.strftime('%Y%m%d'))
        s2 = format(n, 'b')
        if s2 == s2[::-1]:
            ans.append(n)
        d += step

    return ans

ans = solve1('1964-10-10', '2020-07-24')
print(ans)


def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step

def solve2(date_start, date_end):
    ans = []
    start = datetime.strptime(date_start, '%Y-%m-%d').date()
    end = datetime.strptime(date_end, '%Y-%m-%d').date()
    step = timedelta(days=1)
    for d in date_range(start, end, step):
        n = int(d.strftime('%Y%m%d'))
        s2 = format(n, 'b')
        if s2 == s2[::-1]:
            ans.append(n)
        d += step

    return ans

ans = solve2('1964-10-10', '2020-07-24')
print(ans)



def solve3(date_start, date_end):
    ans = []
    start = int(datetime.strptime(date_start, '%Y-%m-%d').date().strftime('%Y%m%d'))
    end = int(datetime.strptime(date_end, '%Y-%m-%d').date().strftime('%Y%m%d'))
    for i in range(start, end):
        s2 = format(i, 'b')
        if s2 == s2[::-1]:
            try:
                d = datetime.strptime(str(i), '%Y%m%d').date()
                ans.append(i)
            except:
                ...

    return ans

ans = solve3('1964-10-10', '2020-07-24')
print(ans)
