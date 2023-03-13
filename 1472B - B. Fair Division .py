'''

1472B - B. Fair Division


'''

for i in range(int(input())):
    temp=int(input())
    arr=[int(arr) for arr in input().split()]
    if(sum(arr)%2==1):
        print("NO")
    else:
        count1=arr.count(1)
        count2=arr.count(2)
        if (count2 %2==0 and count1 %2==0  ):
            print("YES")
        elif(count2%2==1 and count1==0):
            print("NO")
        else:
            print("YES")
           