'''
791A - A. Bear and Big Brother
 
'''
a,b= input().split()
a=int(a)
b=int(b)
count=0
 
while a<=b:
    count=count+1
    a=a*3
    b=b*2
 
 
print(count)