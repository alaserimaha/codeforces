'''

935A - A. Fafa and his Company

'''
temp=int(input())
count=0
for i in range(1,temp//2+1):
    if temp%i==0:
        count=count+1
print(count)