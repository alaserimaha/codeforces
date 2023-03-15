'''

1542A - A. Odd Set

'''
for i in range(int(input())):
    temp=int(input())
    arr=[int(arr) for arr in input().split()]
    counteven=0
    countodd=0
    for i in arr:
        if(i%2==0):
            counteven=counteven+1
        else:
            countodd=countodd+1
    if(countodd==counteven):
        print('Yes')
    else:
        print("No")