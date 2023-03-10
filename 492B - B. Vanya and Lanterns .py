'''
492B - B. Vanya and Lanterns

'''
n,l=map(int, input().split())
arr=[int(arr) for arr in input().split()]
arr=sorted(arr)
m=0
for i in range(n-1):
    if(arr[i+1]-arr[i]>m):
        m=arr[i+1]-arr[i]
re=max(arr[0],m/2,l-arr[n-1])
print(re)
