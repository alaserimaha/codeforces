'''

1512A - A. Spy Detected!

'''

a=int(input())
for i in range(a):
    num=int(input())
    arr=[int(arr) for arr in input().split()]
    newarr=list(arr)
    newarr.sort()
    if(newarr.count(newarr[0])>1):
        print(arr.index(newarr[len(newarr)-1])+1)
    else:
        print(arr.index(newarr[0])+1)