'''

467B - B. Fedor and New Game


'''
a,b,c= map(int, input().split())
arr=[]
for i in range(b+1):
    n=int(input())
    arr.append(n)
count=0
for i in arr[:-1]:
    re=bin(arr[-1]^i)
    if str(re[2:]).count('1')<=c:
        count=count+1  
print(count)  
        