'''

1690A - A. Print a Pedestal (Codeforces logo?)


'''
for i in range(int(input())):
    n=int(input())
    if(n%3==0):
        print(n//3, n//3+1, n//3-1)
    elif(n%3==1):
        print(n//3, n//3+2, n//3-1) 
    elif(n%3==2):
        print(n//3+1, n//3+2, n//3-1)