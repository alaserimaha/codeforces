'''
344A - A. Magnets

'''
temp=""
total=0
for i in range(int(input())):
    a=input()
    if(a!=temp):
        total=total+1
        temp=a
print(total)