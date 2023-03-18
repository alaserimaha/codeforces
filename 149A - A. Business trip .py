'''

149A - A. Business trip


'''
a=int(input())
arr=[int(arr) for arr in input().split()]
if(sum(arr)<a):
    print(-1)
else:
    arr.sort()
    total=0
    s=0
    while True:
        if(s>=a):
            break
        else:
            total=total+1
            s=s+arr.pop()
    print(total)
            