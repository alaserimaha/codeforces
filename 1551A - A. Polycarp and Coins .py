'''

1551A - A. Polycarp and Coins


'''

for i in range(int(input())):
    coin =int(input())
    if(coin%3==0):
        print(coin//3, coin//3)
    else:
        if(coin/3>(coin//3+0.5)):
            print(coin//3, coin//3+1)
        else:
            print(coin//3+1, coin//3)
           