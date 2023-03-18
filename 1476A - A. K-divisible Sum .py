'''

1476A - A. K-divisible Sum

'''
for i in range(int(input())):
    n,k=map(int,input().split())
    if n>=k:
        if(n%k==0):
            print(1)
        else:
            print(2)  
    elif(n==1):
        print(k)
    else:
        if(k%n==0):
            print(k//n)
        else:
            print((k-(k//n)*n)//n+k//n+1)