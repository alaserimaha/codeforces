'''
1A - A. Theatre Square

'''

n,m,a=map(int , input().split())
total1=0
total2=0
 
if(n%a==0):
    total1=total1+n//a
else:
    total1=total1+n//a+1
if(m%a==0):
    total2=total2+m//a
else:
    total2=total2+m//a+1
print(total1*total2)