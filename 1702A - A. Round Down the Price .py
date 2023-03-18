'''

1702A - A. Round Down the Price


'''
import bisect
i=0
arr=[]
while 10**i<10**10:
    arr.append(10**i)
    i=i+1
for i in range(int(input())):
    n=int(input())
    print(n-arr[bisect.bisect(arr,n)-1])