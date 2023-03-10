'''
1409A - A. Yet Another Two Integers Problem

'''
a=int(input())
re=[]
arr=[]
for i in range(a):
    a,b=input().split()
    if(a==b):
         re.append(0)
    else: 
        count=(abs(int(a)-int(b))/10)
        if(count>(abs(int(a)-int(b))//10)):
            re.append(int(count)+1)
        else:
            re.append(int(count))
            
for i in re:
    print(i)