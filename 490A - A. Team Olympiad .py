'''

490A - A. Team Olympiad

'''

a=int(input())
arr=[int(arr) for arr in input().split()]
teams=[]
count=min(arr.count(1),arr.count(2),arr.count(3))
print(count)
for i in range(count):
    teams.append(arr.index(1)+1)
    teams.append(arr.index(2)+1)
    teams.append(arr.index(3)+1)
    arr[arr.index(1)]=0
    arr[arr.index(2)]=0
    arr[arr.index(3)]=0
for i in range(0,count*3,3):
    print(teams[i],teams[i+1],teams[i+2])
    