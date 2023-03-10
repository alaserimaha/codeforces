'''
427A - A. Police Recruits

'''
a=int(input())
b=[int(b) for b in input().split()]
re=0
count=0
for i in b:
    if(i==-1):
        if(count>0):
            count=count-1
        else:
            re=re+1
    if(i>0):
        count=count+i
        
print(re)
