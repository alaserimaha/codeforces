'''

1294A - A. Collecting Coins

'''
for i in range(int(input())):
    arr=[int(arr) for arr in input().split()]
    n=arr.pop()
    m=max(arr)
    arr=abs(sum([int(i)-m for i in arr]))
    if(arr>n):
        print("NO")
    elif((n-arr )%3==0):
        print("YES")
    else:
        print("NO")
   