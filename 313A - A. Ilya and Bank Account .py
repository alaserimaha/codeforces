'''

313A - A. Ilya and Bank Account

'''

a=int(input())
if a>=0:
    print(a)
else:
    b=str(a)
    if(int(b[:-1])>int(b[:-2]+b[-1])):
        b=b[:-1]
        print(int(b))
    else:
        b=b[:-2]+b[-1]
        print(int(b))