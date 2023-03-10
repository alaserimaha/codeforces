'''
466A - A. Cheap Travel


'''
x=[int(a) for a in input().split()]
n, m, a, b=x
count1=a*n
count2=0
temp=n
count3=0
while temp>0:
    temp=temp-m
    count3=count3+b
while n-m>=0:
    count2=count2+b
    n=n-m
while n-1>=0:
    count2=count2+a
    n=n-1
print(min(count1,count2,count3))