'''

124A - A. The number of positions


'''
a,b,c=map(int , input().split())
if(b+c>=a):
    print(a-b)
else:
    print(c+1)