'''
1618A - A. Polycarp and Sums of Subsequences

'''

for i in range(int(input())):
    arr=[int(arr) for arr in input().split()]
    if(arr[0]+arr[1]==arr[2]):
        print(arr[0],arr[1],arr[3])
    else:
        print(arr[0],arr[1],arr[2])