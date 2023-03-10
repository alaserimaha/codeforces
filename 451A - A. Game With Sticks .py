'''
451A - A. Game With Sticks

'''
a,b=input().split()
a=int(a)
b=int(b)
boole=True
while a*b>0:
    a=a-1
    b=b-1
    boole=not boole
if (boole==True):
    print("Malvika")
else:
    print("Akshat")