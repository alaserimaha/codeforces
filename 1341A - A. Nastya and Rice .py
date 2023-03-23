'''

1341A - A. Nastya and Rice

'''

for i in range(int(input())):
    n,a,b,c,d=map(int, input().split())
    start=c+d
    end=c-d
    s=a+b
    e=a-b
    count1=s*n
    count2=e*n
    if (start>=count1>=end or start>=count2>=end or (count1>start and count2<end)):
        print("Yes")
    else:
        print('No')