'''

459B - B. Pashmak and Flowers


'''

input()
arr=[int(arr) for arr in input().split()]
if(max(arr)==min(arr)):
    n=arr.count(max(arr))-1
    print(0, (n * (n + 1) // 2))
else:
    print(max(arr)-min(arr), (arr.count(max(arr)))*(arr.count(min(arr))))