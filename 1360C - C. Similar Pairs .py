'''
1360C - C. Similar Pairs

'''

for i in range(int(input())):
    a=int(input())
    arr=[int(arr) for arr in input().split()]
    re='NO'
    ev=[i for i in arr if i%2==0]
    od=[i for i in arr if i%2==1]
    if(len(ev)%2==0 and len(od)%2==0 ):
        re='YES'
    else:
        for i in ev:
            if (i+1 in od or  i-1 in od):
                re="YES"
                break
    print(re)