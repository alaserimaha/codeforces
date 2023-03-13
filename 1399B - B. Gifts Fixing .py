'''

1399B - B. Gifts Fixing


'''
for i in range(int(input())):
    temp=int(input())
    a=[int(arr) for arr in input().split()]
    b=[int(arr) for arr in input().split()]
    valuea=min(a)
    valueb=min(b)
    total=0
    for i in range(temp):
        if a[i]>valuea and  b[i]>valueb:
            c=min(a[i]-valuea ,b[i]-valueb)
            a[i]=a[i]-c
            b[i]=b[i]-c
            total=total+c
        total=total+a[i]-valuea+b[i]-valueb
    print(total)