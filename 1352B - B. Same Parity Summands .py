'''

1352B - B. Same Parity Summands


'''
for i in range(int(input())):
    n,k=map(int, input().split())
    if(n%k==0):
        print("YES")
        print((str(n//k)+" ")*k)
    else:
        arr1=[1 for i in range(k)]
        arr2=[2 for i in range(k)]
        if((n-k)%2==0 and n-k>0):
            arr1.pop()
            arr1.append(1+n-k)
            print("YES")
            print(*arr1)
        elif((n-(k*2))%2==0 and (n-(k*2))>0 ):
            arr2.pop()
            arr2.append(2+n-(k*2))
            print("YES")
            print(*arr2)
        else:
            print("NO")