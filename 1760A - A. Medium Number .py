'''

1760A - A. Medium Number

'''
for i in range(int(input())):
    arr=[int(arr) for arr in input().split()]
    arr.remove(max(arr))
    arr.remove(min(arr))
    print(*arr)