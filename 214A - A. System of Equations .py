'''
214A - A. System of Equations

'''

a,b=map(int , input().split())
count=0
for i in range(min(a,b)+1):
    for j in range(min(a,b)+1):
        if(i**2 + j ==a and i+j**2 ==b):
            count=count+1
print(count)