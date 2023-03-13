'''

500A - A. New Year Transportation


'''

n,t=input().split()
n=int(n)
t=int(t)
arr=[int(arr) for arr in input().split()]
i=0
while i < t-1:
    i=i+arr[i]
if(i==(t-1)):
    print("YES")
else:
    print("NO")