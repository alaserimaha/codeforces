'''

32B - B. Borze

'''

a=input()
re=""
i=0
while i < len(a):
    if(a[i]=='.'):
        re=re+"0"
        i=i+1
    elif(a[i:i+2]=="-."):
        re=re+"1"
        i=i+2
    elif(a[i:i+2]=="--"):
        re=re+"2"
        i=i+2

print(re)
        