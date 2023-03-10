'''
750A - A. New Year and Hurry

'''
a,b=input().split()
a=int(a)
b=int(b)
time=240-b
count=0
temp=1
while a>0:
    if(time-temp*5>=0):
        time=time-temp*5
        a=a-1
        count=count+1
        temp=temp+1
    else:
        break
print(count)