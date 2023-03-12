'''

1475A - A. Odd Divisor


'''

def find_del(a):
    a=int(a)
    while a % 2 == 0:
        a = a // 2
    return 'YES' if a != 1 else 'NO'
test=int(input())
for i in range(test):
    temp=int(input())
    print(find_del(temp))