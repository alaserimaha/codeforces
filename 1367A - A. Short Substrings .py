'''

1367A - A. Short Substrings

'''

a=int(input())
re=[]
for i in range(a):
    news=""
    s=input()
    if(len(s))==2:
        re.append(s)
    else:
        news=news+s[0]
        for i in range(1,len(s),2):
            news=news+s[i]
        re.append(news)
for i in re:
    print(i)
            