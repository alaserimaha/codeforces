'''

1703C - C. Cypher

'''
for i in range(int(input())):
    n=int(input() )
    arr=[int(arr) for arr in input().split()]
    for i in range(n):
        s=input()
        s=s[s.index(" ")+1:]
        d=s.count('U')
        u=s.count('D')
        if(d>u):
                arr[i]=(arr[i]-(d-u))%10-(arr[i]//10)
        elif(u>d):
                arr[i]=(arr[i]+(u-d))%10-(arr[i]//10)
    print(*arr)