'''

1363A - A. Odd Selection


'''
for i in range(int(input())):
    n,x=map(int, input().split())
    arr=[int(arr) for arr in input().split()]
    odd=[i for i in arr if i%2==1]
    even=[i for i in arr if i%2==0]
    if(len(odd)==0 and x>0):
        print("No")
    elif(len(odd)>=x):
        if(x%2==1):
            print("Yes")
        elif(x%2==0 and len(even)>0):
            print("Yes")
        else:
            print("No")
    elif(len(odd)<x):
        if(len(odd)%2==1 and len(even)>=x-len(odd)):
            print("Yes")
        elif(len(odd)%2==0 and len(even)>=x-len(odd)+1):
            print("Yes")
        else:
            print("No")