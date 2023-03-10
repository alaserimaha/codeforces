'''
155A - A. I_love_%username%

'''
a=int(input())
b=[int(b) for b in input().split()]
c=[]
re=[]
re2=[]
for i in b:
    if(len(c)==0):
        c.append(i)
        temp=i
    else:
        c.append(i)
        if(max(c)==i):
            re.append(i)
        elif(min(c)==i):
            re.append(i)
for i in re:
    if i not in re2 and i!= temp:
        re2.append(i)
print(len(re2))