'''

1703B - B. ICPC Balloons

'''
for i in range(int(input())):
    input()
    string=input()
    re=[]
    count=0
    for i in string:
        if i in re:
            count=count+1
        else:
            count=count+2
        re.append(i)
    print(count)
            