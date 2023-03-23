'''

1366A - A. Shovels and Swords

'''
for i in range(int(input())):
    a,b=map(int, input().split())
    print(min(a,b,(a+b)//3))