'''

711A - A. Bus to Udayland

'''
arr=[]
flag=True
for i in range(int(input())):
    sub=input()
    if(sub[:2]=='OO' and flag):
        sub='++'+sub[2:]
        arr.append(sub)
        flag=False
    elif(sub[3:]=='OO' and flag):
        sub=sub[:3]+'++'
        arr.append(sub)
        flag=False
    else:
        arr.append(sub)
if(flag==True):
    print("NO")
else:
    print('YES')
    for i in arr:
        print(i)