'''

1360D - D. Buying Shovels

'''

import math
for i in range(int(input())):
    n,k=map(int, input().split())
    re=int(n)
    for i in range(1,int(n**0.5)+1):
        if(n%i==0):
            if(i<=k):
                re=min(re,n//i)
            if(n//i<=k):
                re=min(re,i)
    print(re) 