'''

1541A - A. Pretty Permutations

'''
for i in range(int(input())):
    a=(int(input()))
    arr=[]
    if a%2==0:
        for i in range(2,a+1,+2):
            arr.append(i)
            arr.append(i-1)
    else:
        arr=[3,1,2]
        for i in range(4,a+1,2):
            arr.append(i+1)
            arr.append(i)
    print(*arr)