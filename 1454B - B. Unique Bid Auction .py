'''

1454B - B. Unique Bid Auction

'''
for i in range(int(input())):
    a=int(input())
    arr=[int(i) for i in input().split()]
    re=[0 for i in range(a)]
    for i in arr:
        re[i-1]=re[i-1]+1
    if 1 in re:
        print(arr.index(re.index(1)+1)+1)
    else:
        print(-1)