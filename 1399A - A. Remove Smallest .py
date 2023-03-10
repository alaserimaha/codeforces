'''
1399A - A. Remove Smallest

'''
a=int(input())
re=[]
arr=[]
 
 
for y in range(a):
    arr.clear()
    temp=int(input())
    arr=[int(arr) for arr in input().split()]
    arr.sort()
    i=0
    j=i+1
    while j<len(arr):
        if (arr[j]-arr[i]<= 1):
            arr.remove(arr[i])
        else:
            i=i+1
            j=j+1
            
    if len(arr)==1:
        re.append("YES")
    else:
        re.append("NO")
for u in re :
    print(u)