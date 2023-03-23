'''

450A - A. Jzzhu and Children

'''
n,m=input().split()
n=int(n)
m=int(m)
arr=[int(arr) for arr in input().split()]
for i in range(n):
    if(arr[i]%m==0):
        arr[i]=arr[i]/m 
    else:
        arr[i]=arr[i]//m+1 
arr=arr[::-1]
val=(n)-arr.index(max(arr))
if(arr[n-val]>1):
    print(val)
else:
    print(n)