'''

1669B - B. Triple


'''
for i in range(int(input())):
    n=int(input())
    arr=[int(arr) for arr in input().split()]
    if(n<3):
        re=-1
    else:
        arr.sort()
        re=-1
        for i in range(n-2):
            if(arr[i]==arr[i+2]):
                re=arr[i]
                break
    print(re)