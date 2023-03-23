'''

1632A - A. ABC

'''
for i in range(int(input())):
    a=int(input())
    b=input()
    if(a>=3):
        print('NO')
    else:
        if(b.count('1')<=1 and b.count('0')<=1):
            print("YES")
        else:
            print("NO")