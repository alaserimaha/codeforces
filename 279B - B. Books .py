'''

279B - B. Books

'''
get_input = lambda: map(int, input().split())
n, t = map(int, input().split())
a = [int(i) for i in input().split()]
if n == 1 and a[0] <= t:
    print (1)
else:
    res = 0
    buf = 0
    for i in range(n):
        if buf + a[i] > t:
            break
        buf += a[i]
        res += 1

    for i in range(0, n):
        if i + res >= n:
            break
        buf = buf - a[i] + a[i+res]
        while True:
            if i + res + 1 >= n:
                break
            if buf + a[i+res+1] > t:
                break
            buf += a[i+res+1]
            res += 1
    print (res)