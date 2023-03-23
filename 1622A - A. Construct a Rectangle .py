'''

1622A - A. Construct a Rectangle

'''

for i in range(int(input())):
    arr=[int(i) for i in input().split()]
    m=min(arr)
    arr.remove(m)
    x=max(arr)
    arr.remove(x)
    y=arr[0]
    if(x-m==y):
        print('YES')
    elif(x==y and m%2==0):
        print("YES")
    elif(m==y and x%2==0):
        print("YES")
    else:
        print("NO")