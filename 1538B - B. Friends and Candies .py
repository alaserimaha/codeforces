'''

1538B - B. Friends and Candies

'''
for i in range(int(input())):
    n=int(input())
    arr=[int(arr) for arr in input().split()]
    arr.sort()
    if n==1 or arr[0]==arr[-1]:
        print(0)
    elif(sum(arr)%n!=0):
        print(-1)
    else:
        k=0
        goal=sum(arr)//n
        a=[i for i in arr if i>goal]
        print(len(a))