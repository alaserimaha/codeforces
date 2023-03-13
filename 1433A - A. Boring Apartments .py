'''

1433A - A. Boring Apartments


'''

a=int(input())
for i in range(a):
    stop=input()
    count=1
    temp=""
    total=0
    while (temp)!=stop:
        if(len(temp)>3):
            count=count+1
            temp=str(count)  
            total=total+len(temp)
        else:
            temp=temp+str(count)
            total=total+len(temp)
    print(total)