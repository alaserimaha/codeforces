'''

1624A - A. Plus One on the Subset


'''

a=int(input())
re=[]
for i in range(a):
    temp=int(input())
    arr=[int(arr) for arr in input().split()]
    re.append(max(arr)-min(arr))
for i in re:
    print(i)