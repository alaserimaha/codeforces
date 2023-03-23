'''

1359A - A. Berland Poker

'''
for i in range(int(input())):
    n,m,k=map(int, input().split())
    print(min(m, (n - m) // (k - 1)))