'''

1462A - A. Favorite Sequence

'''
for i in range(int(input())):
    temp=int(input())
    arr=[int(arr) for arr in input().split()]
    re=[]
    while(len(arr)!=0):
        re.append(arr.pop(0))
        if(len(arr)!=0):
            re.append(arr.pop())
    print(*re)