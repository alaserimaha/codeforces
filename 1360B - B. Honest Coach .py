'''

1360B - B. Honest Coach


'''

for i in range(int(input())):
    n=int(input())
    arr=[int(arr) for arr in input().split()]
    arr.sort()
    m=arr[1]-arr[0]
    for i in range(2,n):
        t=arr[i]-arr[i-1]
        if( t==0 ):
            m=t
            break
        else:
            if(t<m):
                m=t
    print(m)