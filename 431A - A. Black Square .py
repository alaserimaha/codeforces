'''

431A - A. Black Square


'''

arr=[int(arr) for arr in input().split()]
arr2=list(input())
total=0
for i in arr2:
    total =total+arr[int(i)-1]
print(total)   