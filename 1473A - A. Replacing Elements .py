'''

1473A - A. Replacing Elements


'''
for i in range(int(input())):
    n,d=map(int, input().split())
    arr=[int(arr) for arr in input().split()]
    if(max(arr)<=d):
        print("YES")
    else:
        
        m=min(arr)
        m2=0
        arr.remove(min(arr))
        if(len(arr)!=0):
            m2=min(arr)
        if(m+m2 <= d):
            print("YES")
        else:
            print("NO")