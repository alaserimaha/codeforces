'''

1551B1 - B1. Wonderful Coloring - 1

'''

for i in range(int(input())):
    arr=(sorted(input()))
    r=''
    g=''
    flag=True
    for i in range(len(arr)):
        if(i==len(arr)-1):
            if(arr[i] not in r and flag):
                r=r+arr[i]
                flag=False
            elif(arr[i] not in g and not flag):
                g=g+arr[i]
                flag=True
        elif(arr[i]==arr[i+1] and arr[i] not in r):
            r=r+arr[i]
            g=g+arr[i]
        elif(arr[i] not in r and flag):
            r=r+arr[i]
            flag=False
        elif(arr[i] not in g and not flag):
            g=g+arr[i]
            flag=True
    print(min(len(r), len(g)))