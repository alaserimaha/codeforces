'''

456A - A. Laptops

'''

a=[]
b=[]
temp=int(input())
for i in range(temp):
    num1,num2=map( int , input().split())
    a.append(num1)
    b.append(num2)
re="Poor Alex"
for i in range(temp):
    if(a[i]!=b[i]):
        re="Happy Alex"
        break       
print(re)