'''
144A  - A. Arrival of the General

'''
x = int(input())
a = [int(item) for item in input().split()]
maxa=max(a)
mina=min(a)
count1=a.index(maxa)

lenth=x-1
while True:
    if a[lenth]==mina:
        count2=lenth
        break
    lenth=lenth-1
if(count1>count2):
    count2=x-count2-1
    print(count1+count2-1)
else:
    count2=x-count2-1
    print(count1+count2)
