'''

1560B - A. Elections


'''
for i in range(int(input())):
    a,b,c=map(int, input().split())
    total=(abs(a-b)*2)
    if(a>total or b>total):
        print(-1)
    elif(c<=total):
        if(c>total//2):
            if(a!=c-total//2 and b!=c-total//2):
                print(c-total//2)
            else:
                print(-1)
        else:
            if(a!=c+total//2 and b!=c+total//2):
                print(c+total//2)
            else:
                print(-1)
    else:
        print(-1)