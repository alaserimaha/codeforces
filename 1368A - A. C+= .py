'''

1368A - A. C+=


'''
for i in range(int(input())):
    a,b,n=map(int, input().split())
    total=0
    while(a<=n and b<=n):
        if(a>b):
            b=b+a
            total=total+1
        else:
            a=a+b
            total=total+1
    print(total)