'''

1353A - A. Most Unstable Array

'''
for i in range(int(input())):
    l,s=map(int, input().split())
    if(l==1):
        print(0)
    elif(l==2):
        print(s)
    else:
        total=l//2   
        count=(s/total)*(l-1)
        if(l%2==0):
            count=count+s/total
        print(round(count))