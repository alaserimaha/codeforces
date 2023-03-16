'''

1385A - A. Three Pairwise Maximums


'''

for i in range(int(input())):
    a,b,c=map(int, input().split())
    if(a==b==c):
        print("YES")
        print(a,b,c)
    elif(a==c and a>b):
        a1=a
        b1=b
        c1=b
        print("YES")
        print(a1,b1,c1)
    elif(b==c and b>a):
        a1=a
        b1=a
        c1=c
        print("YES")
        print(a1,b1,c1)
    elif(a==b and a>c):
        a1=c
        b1=a
        c1=c
        print("YES")
        print(a1,b1,c1)
    else:
        print("NO")