'''

1676B - B. Equal Candies

'''
for i in range(int(input())):
    input()
    arr=[int(arr) for arr in input().split()]
    m=min(arr)
    total=0
    for i in arr:
        total=total+abs(m-i)
    print(total)