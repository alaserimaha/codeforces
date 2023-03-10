'''
1154A - A. Restoring Three Numbers

'''
arr=[ int(a) for a in input().split()]
total=max(arr)
arr.remove(max(arr))
newc=total-arr[0]
newb=total-arr[1]
newa=total-arr[2]
print(newa,newb,newc)