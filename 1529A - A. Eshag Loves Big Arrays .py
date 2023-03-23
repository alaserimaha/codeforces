'''
1529A - A. Eshag Loves Big Arrays

'''
for i in range(int(input())):
    a=int(input())
    arr=[int(i) for i in input().split()]
    arr.sort()
    if(len(arr)==1):
        print(0)
    else:
        
        avr=(arr[0]+arr[1])//2
        arr2=[i for i in arr if i<=avr]
        print(len(arr)-len(arr2))
   