'''

1629A - A. Download More RAM

'''
for i in range(int(input())):
    a,total=map(int, input().split())
    arr=[int(i) for i in input().split()]
    arr2=[int(i) for i in input().split()]
    dic={}
    for i in range(a):
        if(arr[i] in dic.keys()):
            dic[arr[i]]=dic[arr[i]] + arr2[i]
        else:
            dic[arr[i]]=arr2[i]
    myKeys = list(dic.keys())
    myKeys.sort()
    dic = {i: dic[i] for i in myKeys}
    for i in dic.keys():
        if(i<=total):
            total=total+dic[i]
        else:
            break
    print(total)