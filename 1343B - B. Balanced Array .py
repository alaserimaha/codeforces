'''

1343B - B. Balanced Array

'''

for i in range(int(input())):
    num=int(input())
    if(num%4!=0):
        print("NO")
    else:
        print("YES")
        arr=[i for i in range(2,2*(num//2)+1 ,2)]
        arr2=[i for i in range(1,2*(num//2)+1 ,2)]
        arr2[-1]=sum(arr)-sum(arr2[:-1])
        print(*arr,*arr2)