'''

1560A - A. Dislike of Threes


'''

arr=list(range(1,1667))
for i in arr:
    if (str(i)[-1]=='3'):
        arr.remove(i)
for i in arr:
    if(i%3==0):
        arr.remove(i)
re=[]
a=int(input())
for i in range(a):
    temp=int(input())
    re.append(arr[temp-1])
for i in re:
    print(i)