'''

1327A - A. Sum of Odd Integers


'''
for i in range(int(input())):
    a,b=map(int,input().split())
    if( (a%2==0 and b%2==0) and (b*b)<=a):
        print("YES")
    elif ((a%2==1 and b%2==1) and b*b<=a):
        print("YES")
    else:
        print("NO")