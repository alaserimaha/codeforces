'''

1097A - A. Gennady and a Card Game


'''

a=(input())
arr=[(arr) for arr in input().split()]
re="NO"
for i in arr:
    if(a[0]==i[0] or a[1]==i[1]):
        re=("YES")
        break
print(re)