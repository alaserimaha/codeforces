'''

1360A - A. Minimal Square


'''

test=int(input())
for i in range(test):
    a,b=input().split()
    a=int(a)
    b=int(b)
    c=(min(a,b)*2)**2
    d=(max(a,b)**2)
    print(max(c,d))