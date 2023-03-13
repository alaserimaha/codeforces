'''

1352C - C. K-th Not Divisible by n


'''
for i in range(int(input())):
    n,k=map(int, input().split())
    s=0
    e=10**10
    while(e>=s):
        mid=(s+e)//2
        re= mid - mid//n
        if(re==k):
            sol=mid
            e=mid-1
        elif(re>k):
            e=mid-1
        else:
            s=mid+1
    print(sol)