'''

1454A - A. Special Permutation

'''
for i in range(int(input())):
    temp=int(input())
    arr=[i for i in range(temp,0,-1)]
    if(temp%2==1):
        a=arr[temp//2]
        arr[temp//2]=arr[0]
        arr[0]=a
    print(*arr)