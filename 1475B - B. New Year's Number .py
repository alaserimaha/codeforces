'''

1475B - B. New Year's Number


'''
for i in range(int(input())):
    temp=int(input())
    if(temp>=2020 and (temp%2020==0 or temp%2020<=temp//2020)):
        print("YES")
    else:
        print("NO")