'''

1367B - B. Even Array


'''

a=int(input())
re=[]
for a in range(a):
    temp=int(input())
    arr=[int(arr) for arr in input().split()]
    even=0
    odd=0
    move =0
    for i in range(len(arr)):
        if(i%2!=arr[i]%2):
            if (i%2==0):
                even=even+1
            else:
                odd=odd+1
        if (even>0 and odd>0):
            move=move+1
            even=even-1
            odd=odd-1
    if(even>0  or  odd>0):
         re.append(-1)
    else:
        re.append(move)
for i in re:
    print(i)