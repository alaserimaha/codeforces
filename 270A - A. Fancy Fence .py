'''

270A - A. Fancy Fence

'''

arr=[180-(360/arr) for arr in range(3,361)]
for i in range(int(input())):
    temp=float(input())
    if(temp in arr):
        print("YES")
    else:
        print('NO')