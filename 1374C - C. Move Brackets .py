'''

1374C - C. Move Brackets

'''
for i in range(int(input())):
    temp=int(input())
    a=input()
    count=0
    total=0
    for i in a:
        if(i=='('):
            count=count+1
        else:
            count=count-1
        if(count<0):
            total=total+1
            count=count+1
    print(total)