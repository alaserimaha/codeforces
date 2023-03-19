'''

1611A - A. Make Even

'''

for i in range(int(input())):
    a=input()
    if(int(a)%2==0):
        print(0)
    elif(int(a[0])%2==0):
        print(1)
    else:
        re=-1
        for i in a:
            if(int(i)%2==0):
                re=2
                break
        print(re)
   