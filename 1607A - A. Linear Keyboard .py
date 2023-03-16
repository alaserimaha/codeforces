'''

1607A - A. Linear Keyboard


'''

for i in range(int(input())):
    a=input()
    dic=dict(zip(list(a), list(range(1,27))))
    temp=input()
    total=0
    for i in range(1,len(temp)):
        total=total+abs(dic[temp[i]]-dic[temp[i-1]]) 
    print(total)