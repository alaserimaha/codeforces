'''

1567A - A. Domino Disaster

'''

for i in range(int(input())):
    a=int(input())
    s=list(input())
    for i in range(a):
        if(s[i]=='U'):
            s[i]='D'
        elif(s[i]=='D'):
            s[i]='U'
    print(''.join(s))