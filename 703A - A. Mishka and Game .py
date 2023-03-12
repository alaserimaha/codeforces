'''

703A - A. Mishka and Game


'''

a=int(input())
m=0
c=0
for i in range(a):
    a,b=input().split()
    a=int(a)
    b=int(b)
    if a>b:
        m=m+1
    elif b>a:
        c=c+1
if(m>c):
    print('Mishka')
elif(c>m):
    print('Chris')
else:
    print('Friendship is magic!^^')