'''

1397A - A. Juggling Letters

'''

for i in range(int(input())):
    a=int(input())
    s=""
    for j in range(a):
        s=s+input()
    l=0
    
    re='YES'
    s=sorted(s)
    while l<len(s):
        if(s.count(s[l])==a):
            l=l+a
        elif(s.count(s[l])%a==0):
            l=l+a*(s.count(s[l])//a)
        else:
            re='NO'
            break
    print(re)