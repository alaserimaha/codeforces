'''
581A - A. Vasya the Hipster

'''
a,b=input().split()
a=int(a)
b=int(b)
count1=0
count2=0
while a>0 and b>0:
    a=a-1
    b=b-1
    count1=count1+1
if a>1:
    count2=count2+int(a/2)
if b>1:
    count2=count2+int(b/2)
print(count1,count2)