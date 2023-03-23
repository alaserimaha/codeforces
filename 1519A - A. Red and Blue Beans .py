'''

1519A - A. Red and Blue Beans

'''
for i in range(int(input())):
    r,b,d=map(int, input().split())
    if(abs(r-b)<= min(r,b)*d):
        print('YES')
    else:
        print('NO')