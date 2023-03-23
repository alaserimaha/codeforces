'''
433B - B. Kuriyama Mirai's Stones

'''

a=int(input())
arr=[int(i) for i in input().split()]
arr2=[arr[0]]
for i in range(1,a):
    arr2.append((arr[i]+arr2[-1]))
arr3=sorted(arr)
arr4=[arr3[0]]
for i in range(1,a):
    arr4.append((arr3[i]+arr4[-1]))
arr=list(arr2)
arr2=list(arr4)
for i in range(int(input())):
    a,b,c=map(int, input().split())
    if(a==1):
        if(b==1):
            print(arr[c-1])
        else:
            print(arr[c-1]-arr[b-2])
    else:
        if(b==1):
            print(arr2[c-1])
        else:
            print(arr2[c-1]-arr2[b-2])