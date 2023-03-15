'''

1311A - A. Add Odd or Subtract Even

'''
for i in range(int(input())):
    a,b=map(int , input().split())
    count=0
    
    while a!=b:
        if(a<b):
            if ((b-a)%2==1):
                count=count+1
                break
            else:
                count=count+2
                break
        elif(a>b):
            if((a-b)%2==0):
                count=count+1
                break 
            else:
                count=count+2
                break
    print(count)