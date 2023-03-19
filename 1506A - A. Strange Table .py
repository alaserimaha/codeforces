'''

1506A - A. Strange Table

'''

for i in range(int(input())):
    n,m,x=map(int, input().split())
    if(x//n==x/n):
        col=x/n
    else:
        col=x//n+1
    if(x%n==0):
        row=n
    else:
        row=x%n
    val=col+(m*(row-1))
    print(int(val))