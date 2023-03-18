'''

1593A - A. Elections


'''
for i in range(int(input())):
    a,b,c=map(int,input().split())
    if(a<=0 and b<=0 and c<=0):
        print(1,1,1)
    else:
        if(max(a,b,c) ==a and max(a,b,c) ==b):
            print(max(a,b,c)-a+1,max(a,b,c)-b+1,max(a,b,c)-c+1) 
        elif((max(a,b,c) ==b and max(a,b,c) ==c)):
            print(max(a,b,c)-a+1,max(a,b,c)-b+1,max(a,b,c)-c+1) 
        elif((max(a,b,c) ==a and max(a,b,c) ==c) )  :
             print(max(a,b,c)-a+1,max(a,b,c)-b+1,max(a,b,c)-c+1)
        elif(max(a,b,c)==a):
            print(max(a,b,c)-a,max(a,b,c)-b+1,max(a,b,c)-c+1)
        elif(max(a,b,c)==b):
            print(max(a,b,c)-a+1,max(a,b,c)-b,max(a,b,c)-c+1)
        else:
            print(max(a,b,c)-a+1,max(a,b,c)-b+1,max(a,b,c)-c)