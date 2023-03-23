'''

1409B - B. Minimum Product

'''
for i in range(int(input())):
    a,b,x,y,n=map(int,input().split())
    if(a-min(a-x,n)<b-min(b-y,n)):
        temp=int(a-x)
        a=a-min(temp,n)
        n=n-min(temp,n)
        if(n>0):
            temp=int(b-y)
            b=b-min(temp,n)
            n=n-min(temp,n)
    elif(a-min(a-x,n)>b-min(b-y,n)):
        temp=int(b-y)
        b=b-min(temp,n)
        n=n-min(temp,n)
        if(n>0):
            temp=int(a-x)
            a=a-min(temp,n)
            n=n-min(temp,n)
    else:
        if(x<=y):
            temp=int(a-x)
            a=a-min(temp,n)
            n=n-min(temp,n)
            if(n>0):
                temp=int(b-y)
                b=b-min(temp,n)
                n=n-min(temp,n)
        else:
            temp=int(b-y)
            b=b-min(temp,n)
            n=n-min(temp,n)
            if(n>0):
                temp=int(a-x)
                a=a-min(temp,n)
                n=n-min(temp,n)
    print(a*b)