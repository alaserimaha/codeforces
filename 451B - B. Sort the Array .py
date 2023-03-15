'''

451B - B. Sort the Array

'''
temp=int(input())
arr=[int(arr) for arr in input().split()]
sor=(list(arr))
sor.sort()
if(sor==arr):
    print("yes")
    print(1,1)
else:
    
    count=[i for i in range(temp) if arr[i]!=sor[i]]
    t=arr[count[0]:count[-1]+1]
    t=t[::-1]
    arr[count[0]:count[-1]+1]=t
    if(arr==sor):
        print("yes")
        print(count[0]+1,count[-1]+1)

    else:
        print("no")