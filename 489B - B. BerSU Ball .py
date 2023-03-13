'''

489B - B. BerSU Ball


'''

temp1=int(input())
arr1=[int(arr) for arr in input().split()]
temp1=int(input())
arr2=[int(arr) for arr in input().split()]
arr1=sorted(arr1)
arr2=sorted(arr2)
count=0
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if abs(arr1[i]-arr2[j])<2:
            count=count+1
            arr2.remove(arr2[j])
            break
print(count)