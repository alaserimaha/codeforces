'''

707A - A. Brain's Photos


'''
n,m=map(int, input().split())
temp=""
for i in range(n):
    temp=temp+input()
if temp.count('C')>0 or temp.count('M')>0 or  temp.count('Y')>0:
    print('#Color')
else:
    print("#Black&White")