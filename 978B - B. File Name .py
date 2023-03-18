'''

978B - B. File Name


'''
n=int(input())
a=input()
if(a.count('xxx')==0):
    print(0)
else:
    count=0
    while(a.count('xxx')!=0):
        a=a.replace('xxx','xx',a.count('xxx'))
    print(n-len(a))
        