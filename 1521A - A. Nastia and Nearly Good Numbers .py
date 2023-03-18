'''

1521A - A. Nastia and Nearly Good Numbers


'''
for i in range(int(input())):
    a,b=map(int, input().split())
    if(b==1):
        print("NO")
    else:
        z=a*b*2
        x=a
        y=z-a
        print("YES")
        print(x,y,z)