'''

1370A - A. Maximum GCD


'''

import math
a=int(input())
for i in range(a):
    re=0
    num=int(input())
    if(num%2==0):
        re=math.gcd(num,(num//2))
    else:
        re=math.gcd(num-1,(num//2))
    print(re)