'''

1343C - C. Alternating Subsequence


'''
for i in range(int(input())):
    a=int(input())
    arr=[int(arr) for arr in input().split()]
    re=[]
    if(arr[0]>0):
        b=True
    else:
        b=False
    re.append(arr[0])
    for i in arr:
        if(b==True and i<0):
            re.append(i)
            b=False
        elif(b==False and i>0):
            re.append(i)
            b=True
        elif(b==True and i>0):
            if(i>re[-1]):
                re.pop()
                re.append(i)
        elif(b==False and i<0):
            if(i>re[-1]):
                re.pop()
                re.append(i)
            
    print(sum(re))