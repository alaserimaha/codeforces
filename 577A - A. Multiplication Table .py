'''

577A - A. Multiplication Table


'''

n,x=map(int, input().split())
total=0
if(x==1):
    print(1)
else:
    for i in range(1,min(x//2+1 , n)+1):
        if(x%i==0 and x/i<=n):
            total=total+1
    if(x<=n):
        total=total+1
    print(total)