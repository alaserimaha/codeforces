'''

1527A - A. And Then There Were K

'''
import bisect
i=2
arr=[0]
while i<10**9:
    arr.append(i-1)
    i=i*2
for i in range(int(input())):
    print(arr[bisect.bisect_left(arr, int(input()))-1])