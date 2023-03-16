'''

1538A - A. Stone Game


'''
for i in range(int(input())):
    size=int(input())
    arr=[int(arr) for arr in input().split()]
    a=arr.index(1)+1
    b=arr.index(size)+1
    a,b=min(a,b),max(a,b)
    print(min(b,size-a+1,a+size-b+1))