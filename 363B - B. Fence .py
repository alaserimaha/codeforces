'''

363B - B. Fence


'''

a,n=map(int, input().split())
arr=[int(arr) for arr in input().split()]
s=0
s=sum(arr[:n])
mn=s
imn=0
for i in range(1,a-n+1):
    s +=arr[i+n-1]-arr[i-1]
    if s<mn:
        mn=s
        imn=i
print(imn+1)