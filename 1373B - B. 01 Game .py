'''
1373B - B. 01 Game

'''

for i in range(int(input())):
    a=input()
    t=a.count('01')
    y=a.count('10')
    total=0
    while (t>0 or y>0):
        if(t>0):
            total=total+t
            a=a.replace('01',"")
            t=a.count('01')
        else:
            y=a.count('10')
            a=a.replace('10',"")
            total=total+y
            y= a.count('10')
    if(total%2==0):
        print('NET')
    else:
        print('DA')