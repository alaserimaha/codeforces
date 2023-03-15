'''

1535A - A. Fair Playoff

'''

for i in range(int(input())):
    arr=[int(arr) for arr in input().split()]
    num1,num2=sorted(arr)[-2:]
    if((num1 in arr[:2] and num2 in arr[2:]) or (num2 in arr[:2] and num1 in arr[2:] )):
        print("YES")
    else:
        print("NO")