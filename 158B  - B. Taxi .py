'''
158B  - B. Taxi

'''
n=int(input())
arr=[int(arr) for arr in input().split()]
c1=arr.count(1)
c2=arr.count(2)
c3=arr.count(3)
count=arr.count(4)
while(c3!=0):
    if(c1>0):
        m=min(c1,c3)
        count=count+ m
        c1=c1-m
        c3=c3-m
    else:
        count=count+c3 
        c3=0
while(c2!=0):
    if(c2%2==0):
        count=count+(c2//2)
        c2=0
    else:
        count=count+(c2//2)
        c2=c2-((c2//2)*2)
    if(c2>0 and c1>1):
        count=count+1
        c2=0
        c1=c1-2
    elif(c2>0 and c1==1):
        count=count+1
        c2=0
        c1=0
    elif(c2>0):
        count=count+1
        c2=0
while(c1!=0):
    if(c1%4==0):
        count=count+(c1//4)
        c1=0
    else:
        count=count+(c1//4)+1
        c1=0
print(count)  