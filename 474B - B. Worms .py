'''

474B - B. Worms

'''
L=[]
input()
r=1
for k in input().split():
    L+=[r]*int(k)
    r+=1
input()
for j in input().split():
    print(L[int(j)-1])