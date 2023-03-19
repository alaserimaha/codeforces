'''

1692C - C. Where's the Bishop?

'''

for i in range(int(input())):
    input()
    f1=False
    f2=False
    for j in range(8):
        a=input()
        if(f1==False and a.count('#')==2):
            f1=True
        elif(f1==True and f2==False and a.count('#')==1):
            re=[j+1 , a.index('#')+1]
            f2=True
    print(*re)