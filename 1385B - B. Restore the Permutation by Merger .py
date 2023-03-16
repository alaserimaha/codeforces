'''

1385B - B. Restore the Permutation by Merger


'''

for i in range(int(input())):
    temp=input()
    arr=[int(arr) for arr in input().split()]
    re=[]
    for i in arr:
        if i not in re:
            re.append(i)
    print(*re)