'''

1709A - A. Three Doors

'''
for i in range(int(input())):
    a=int(input())
    arr=[int(i) for i in input().split()]
    if(a!=0 and arr[a-1]!=0 and arr[arr[a-1]-1]!=0):
        print("YES")
    else:
        print('NO')