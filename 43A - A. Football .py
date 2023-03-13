'''

43A - A. Football


'''

arr=dict()
for i in range(int(input())):
    temp=input()
    if temp in arr.keys():
        arr[temp]=arr[temp]+1
    else:
        arr[temp]=1

max_value = max(arr, key=arr.get)
print(max_value)