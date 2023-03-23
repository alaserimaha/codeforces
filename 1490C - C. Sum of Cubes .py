'''

1490C - C. Sum of Cubes

'''

arr=[i**3 for i in range(1,10000)]
arr=arr+arr
def printPairs(arr, arr_size, sum):
    hashmap = {}
    for i in range(0, arr_size):
        temp = sum-arr[i]
        if (temp in hashmap):
            print('YES')
            return
        hashmap[arr[i]] = i
    print("NO")
for i in range(int(input())):
    a=int(input())
    printPairs(arr,len(arr),a)  