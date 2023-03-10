'''
4C - C. Registration system

'''
a=int(input())
dic=dict()
for i in range(a):
    temp=input()
    if(temp in dic):
        dic[temp]=dic[temp]+1
        print(temp+str(dic[temp]-1))
    else:
        print("OK")
        dic[temp]=1