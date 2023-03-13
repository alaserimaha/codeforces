'''

1520A - A. Do Not Be Distracted!


'''

a=int(input())
re=[]
for i in range(a):
    temp=int(input())
    string=input()
    dic=dict()
    persev=""
    value="YES"
    for i in string:
        if(i not in dic.keys()):
            dic[persev]=False
            dic[i]=True
            persev=i
        else:
            if(dic[i]==False):
                value="NO"
                break
    re.append(value)
        
                
for i in re:
    print(i)  