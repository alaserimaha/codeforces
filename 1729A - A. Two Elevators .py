'''

1729A - A. Two Elevators


'''

for i in range(int(input())):
    a,b,c=map(int, input().split())
    if(a==1):
        print(1)
    elif(abs(b-c)+c==a):
        print(3)
    elif(abs(b-c)+c>a):
        print(1)
    elif(abs(b-c)+c<a):
        print(2)
        