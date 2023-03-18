'''

1650A - A. Deletions of Two Adjacent Letters


'''
for i in range(int(input())):
    s=input()
    t=input()
    if(s.count(t)==0):
        print("NO")
    elif(s.count(t)==1):
        if(len(s[:s.index(t)])%2==0 and len(s[s.index(t)+1:])%2==0):
            print("YES")
        else:
            print("NO")
    else:
        re=[i for i, x in enumerate(s) if x == t]
        res="NO"
        for i in re:
            if(len(s[:i])%2==0 and len(s[i+1:])%2==0):
                res="YES"
                break
        print(res)
                
        