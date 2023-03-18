'''

686A - A. Free Ice Cream


'''
n,x=map(int, input().split())
dip=0
for i in range(n):
    a=input()
    if(a[0]=='+'):
        x=x+int(a[2:])
    else:
        if(x>=int(a[2:])):
            x=x-int(a[2:])
        else:
            dip=dip+1
print(x,dip)