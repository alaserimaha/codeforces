'''

1537A - A. Arithmetic Array


'''
for i in range(int(input())):
    a=int(input())
    arr=[int(arr) for arr in input().split()]
    if(sum(arr)/a==1):
        print(0)
    elif(sum(arr)/a>1):
        print(sum(arr)-a)
    elif(sum(arr)/a<1):
        print(1)