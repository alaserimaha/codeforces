'''

1619B - B. Squares and Cubes

'''

import bisect
arr=[]
for i in range(1,31622+1):
    if(i<=999+1):
        arr.append(i**2)
        arr.append(i**3)
    else:
        arr.append(i**2)
targetList = list(set(arr))
targetList.sort()
for i in range(int(input())):
    a=int(input())
    if(a in targetList ):
        print(targetList.index(a)+1)
    else:
        print(bisect.bisect_left(targetList, a))
    