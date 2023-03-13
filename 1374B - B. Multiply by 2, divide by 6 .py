'''

1374B - B. Multiply by 2, divide by 6


'''
for i in range(int(input())):
    temp=int(input())
    if (temp==1):
        print(0)
    elif(temp%3 != 0):
        print(-1)
    else:
        count=0
        while(temp != 1):
            if(temp %3 !=0):
                print(-1)
                break
            elif (temp%6==0):
                temp=temp/6
                count=count+1
            else:
                temp=temp*2
                count=count+1 
        if(temp==1):
            print(count)