'''
580A  - A. Kefa and First Steps

'''
from queue import Empty
 
 
a=int(input())
count=0
re=[]
arr = list(map(int, input().split()))
for i in range(a-1):
    if(arr[i]<=arr[1+i]):
        count=count+1
        re.append(count)
    else:
        count=0
    
if(not (re)):
    print(1)
else:
    print(max(re)+1)