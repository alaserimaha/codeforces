'''

1490A - A. Dense Array

'''

for i in range(int(input())):
    n=int(input())
    arr=[int(arr) for arr in input().split()]
    count=0
    l=len(arr)
    i=1
    while i<l:
        if(arr[i]>arr[i-1]):
            if(arr[i]/arr[i-1])>2:
                arr.insert(i,(arr[i-1]*2))
                count=count+1
                l=l+1
            else:
                i=i+1
        elif(arr[i]<arr[i-1]):
            if(arr[i-1]/arr[i])>2:
                arr.insert(i,(arr[i]*2))  
                count=count+1
                l=l+1
            else:
                i=i+1
        else:
            i=i+1            
    print(count)