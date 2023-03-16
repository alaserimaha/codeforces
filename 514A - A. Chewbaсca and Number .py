'''

514A - A. Chewbaсca and Number


'''

a=(input())
re=""
for i in range(len(a)):
    if(i==0 and int(a[i])==9):
        re=re+a[i]
    else:
        if(9-int(a[i])<int(a[i])):
            re=re+str(9-int(a[i]))
        else:
            re=re+a[i]
print(re)
         