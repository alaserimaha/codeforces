'''

758A - A. Holiday Of Equality

'''

a=int(input())
arr=[int(arr) for arr in input().split()]
ma=max(arr)
count=0
for i in arr:
    count=count+(ma-i)
print(count)