'''

233A - A. Perfect Permutation


'''

a=int(input())
if(a==1 or a==0 or a%2==1):
     print(-1)
else:
    arr=[]
    b=True
    for i in range(1,a+1):
        if(b==True):
            arr.append(i+1)
            b=False
        else:
            arr.append(i-1)
            b=True
    print(*arr)