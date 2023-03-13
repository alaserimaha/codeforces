'''

1353B - B. Two Arrays And Swaps


'''

a=int(input())
re=[]
for i in range(a):
    n,k=input().split()
    n=int(n)
    k=int(k)
    arr1=[int(arr1) for arr1 in input().split()]
    arr2=[int(arr2) for arr2 in input().split()]
    arr1.sort()
    r1=0
    newarr=[]
    if(k==0):
        re.append(sum(arr1))
    else:
        while len(newarr) < n:
            if (k>0):
                m1=max(arr1)
                m2=max(arr2)
                if (m1>=m2):
                    newarr.append(arr1.pop(arr1.index(m1)))
                else:
                    newarr.append(arr2.pop(arr2.index(m2)))
                    k=k-1 
            else:
                newarr=newarr+arr1[len(arr1)-1:len(arr1)-1-(n-len(newarr)):-1]
        re.append(sum(newarr))
for i in re:
    print(i)