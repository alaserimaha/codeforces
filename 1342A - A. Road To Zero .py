'''

1342A - A. Road To Zero


'''

for i in range(int(input())):
    total=0
    x,y=map(int,input().split())
    a,b=map(int,input().split())
    if(x==0 and y ==0):
        print(0)
    elif(x==0 or y ==0):
        print(a*max(x,y))
    else:
        if(b<=a*2):
            total=total+min(x,y)*b
            m=min(x,y)
            x=x-m
            y=y-m
            total=total+max(x,y)*a
            print(total)
        else:
            total=total+(a*x)+(a*y)
            print(total)