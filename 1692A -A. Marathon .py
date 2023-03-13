'''

1692A -A. Marathon


'''

for i in range(int(input())):
    arr=[int(arr) for arr in input().split()]
    c=len([i for i in arr[1:] if arr[0]<=i ])
    print(c)