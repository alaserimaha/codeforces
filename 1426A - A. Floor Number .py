'''

1426A - A. Floor Number

'''

for i in range(int(input())):
    n,k=map(int, input().split())
    if(n<=2):
        print(1)
    else:
        if((n-2)%k==0):
            print((n-2)//k +1)
        else:
            print((n-2)//k +2)