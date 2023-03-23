'''

1631A - A. Min Max Swap

'''

for i in range(int(input())):
    a=int(input())
    arr=[int(i) for i in input().split()]
    arr2=[int(i) for i in input().split()]
    new=[]
    new2=[]
    for i in range(a):
        if(arr[i] > arr2[i]):
            new.append(arr[i])
            new2.append(arr2[i])

        else:
            new2.append(arr[i])
            new.append(arr2[i])
    print(max(new)*max(new2))