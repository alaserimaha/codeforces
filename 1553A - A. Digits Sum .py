'''

1553A - A. Digits Sum

'''

for i in range(int(input())):
    a=int(input())
    if(a<9):
        print(0)
    elif(a==9):
        print(1)
    else:
        if(str(a)[-1]=='9'):
            print(int(str(a)[:-1])+1)
        else:
            print(int(str(a)[:-1]))