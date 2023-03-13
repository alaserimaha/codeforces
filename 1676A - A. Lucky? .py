'''

1676A - A. Lucky?


'''

for i in range(int(input())):
    temp=[int(arr) for arr in input()]
    if(sum(temp[0:3])==sum(temp[3:])):
        print("YES")
    else:
        print('NO')