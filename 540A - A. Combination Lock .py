'''

540A - A. Combination Lock

'''
a=int(input())
org=input()
goal=input()
count=0
re=0
for i in range(a):
    if(int(org[i])>int(goal[i])):
        re=min(int(org[i])-int(goal[i]) ,10-int(org[i])+int(goal[i]))
    elif(int(org[i]) < int(goal[i])) :
        re=min(int(goal[i])-int(org[i]), 10-int(goal[i])+int(org[i]))
    else:
        re=0
    count=count+re
print(count)
    