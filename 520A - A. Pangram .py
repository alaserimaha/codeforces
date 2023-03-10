'''
520A - A. Pangram

'''

a=int(input())
b=input()
arr=[]
b=b.lower()
for i in range(a):
    if(b[i] not in arr):
        arr.append(b[i])
if(len(arr)==26):
    print("YES")
else:
    print("NO")