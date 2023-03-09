'''
148A  - A. Insomnia cure

'''
a=int(input())
b=int(input())
c=int(input())
d=int(input())
f=int(input())
count=0
for i in range(1,f+1):
    if(i%a==0):
        count=count+1
    elif(i%b==0):
        count=count+1
    elif(i%c==0):
        count=count+1
    elif(i%d==0):
        count=count+1
 
 
print(count)