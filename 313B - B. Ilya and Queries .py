'''

313B - B. Ilya and Queries

'''
s=input()
re=[]
total=0
re.append(total)
for i in range(len(s)-1):
    if(s[i]==s[i+1]):
        total=total+1
    re.append(total)
for i in range(int(input())):
    a,b=map(int,(input().split()))
    print(re[b-1]-re[a-1])