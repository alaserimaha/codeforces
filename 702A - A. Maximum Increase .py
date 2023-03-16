'''

702A - A. Maximum Increase


'''

temp=int(input())
arr=[int(arr) for arr in input().split()]
m=1
re=[]
if(len(arr)==1):
    re.append(1)
else:
    for i in range(1,temp):
        if arr[i]>arr[i-1]:
            m=m+1
        else:
            re.append(m)
            m=1
        re.append(m)
print(max(re))