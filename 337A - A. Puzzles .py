'''
337A - A. Puzzles

'''

n,m=map(int, input().split())
arr=[int(arr) for arr in input().split()]
arr=sorted(arr)
i=0
j=n-1
m=arr[j]-arr[i]
while j <len(arr):
    if(arr[j]-arr[i]<m):
        m=arr[j]-arr[i]
    i=i+1
    j=j+1
print(m)