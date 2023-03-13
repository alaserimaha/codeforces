'''

489C - C. Given Length and Sum of Digits...


'''

m,s=map(int, input().split())
if(m==1 and s==0):
    print(0,0)
elif(9*m<s or s==0):
    print(-1 , -1)
else:
    num1="0"
    s2=int(s)
    while ((sum(list(map(int,num1)))) < s2 and s>0):
        if(s>9):
            num1=num1+"9"
            s=s-9
        else:
            num1=num1+str(s)
            s=0
    num1=num1[1:]
    if(s==0 and len(num1)<m):
        num1=num1+"0"*(m-len(num1))
    num2="0"
    s=int(s2)
    while ((sum(list(map(int,num2)))) < s2 and s>1):
        if(s>9):
            num2="9"+num2
            s=s-9
        else:
            num2=str(s-1)+num2
            s=1
    num2=num2[:-1]
    if(s==1 and len(num2)<m):
        num2='1'+"0"*(m-(len(num2)+1))+num2
    else:
        num2=str(int(num2[0])+1)+num2[1:]
    print(num2, num1)