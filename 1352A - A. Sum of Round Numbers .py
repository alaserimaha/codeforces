'''
1352A - A. Sum of Round Numbers

'''
a=int(input())
arr=[]
re=[]
for i in range(a):
    temp=input()
    arr.clear()
    if (temp[1:]!=('0'*(len(temp)-1))):
        for j in range(len(temp)):
            if(int(temp[j])!=0):
                arr.append((temp[j]+("0"*((len(temp)-1)-j))))
        re.append(len(arr))
        re.append(' '.join(arr)) 
 
    else:
        re.append(1)
        re.append(temp)
for i in re:
    print(i) 