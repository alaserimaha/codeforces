'''

1433B - B. Yet Another Bookshelf

'''

for i in range(int(input())):
    a=int(input())
    arr=[int(i) for i in input().split()]
    arr2=arr[::-1]
    num1=arr.index(1)
    num2=a-arr2.index(1)
    print(arr[num1:num2].count(0))