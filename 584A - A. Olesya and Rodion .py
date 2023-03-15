'''

584A - A. Olesya and Rodion

'''
a,b=map(int,input().split())
start=("1"+("0"*(a-1)))
re=-1
while len(start)==a:
    if(int(start)%b==0):
        re=start
        break
    else:
        start=str(int(start)+1)
print(re)