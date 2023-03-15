'''

1472A - A. Cards for Friends

'''
for i in range(int(input())):
    h,w,n=map(int, input().split())
    total=1
    while h%2==0 or w%2==0:
        if( h%2==0):
            total=total*2
            h=h//2
        elif( w%2==0):
            total=total*2
            w=w//2
    if(total>= n or n==1):
        print("YES")
    else:
        print("NO")