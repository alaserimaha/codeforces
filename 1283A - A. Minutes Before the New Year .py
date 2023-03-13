'''

1283A - A. Minutes Before the New Year



'''
total=60*24
for i in range(int(input())):
    a,b=map(int , input().split())
    print(total-((a*60)+b))  