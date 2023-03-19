'''

1675A - A. Food for Animals

'''

for i in range(int(input())):
    a,b,c,x,y=map(int , input().split())
    x=x-a
    y=y-b
    if(x<=0 and y<=0):
        print("YES")
    elif(x>0 and y>0 and (c-(x+y))>=0):
        print("YES")
    elif(x<=0 and y>0 and (c-y)>=0):
        print("YES")
    elif(y<=0 and x>0 and (c-x)>=0):
        print("YES")
    else:
        print("NO")