'''

706B - B. Interesting drink

'''

import bisect
a=int(input())
arr=[int(a) for a in input().split()]
arr=sorted(arr)
re=[]
for i in range(int(input())):
    n=int(input())
    temp=bisect.bisect_right(arr,n,hi=a)
    re.append(temp)
print(*re, sep="\n")