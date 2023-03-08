'''
236A - A. Boy or Girl
 
'''
str_1=input()
a= list(str_1.strip(" "))
result=[]
count=0
for i in a: 
    if i not in result:
        result.append(i)
        count=count+1 
 
if(count%2==0):
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')