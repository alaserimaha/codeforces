'''

977B - B. Two-gram


'''
import re
n=int(input())
a=input()
m=a.count(a[:2])
r=a[:2]
for i in range(1,n-2):
    temp='(?='+a[i:i+2]+')'
    lengh= len([s.start() for s in re.finditer(temp, a)])
    if(lengh>m):
        m=lengh
        r=a[i:i+2]
print(r)