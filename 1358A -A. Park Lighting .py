'''

1358A -A. Park Lighting

'''
for i in range(int(input())):
    a,b=map(int, input().split())
    if(a*b%2==0):
        print(a*b//2)
    else:
        print(a*b//2 +1)