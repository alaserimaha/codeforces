'''

9A - A. Die Roll


'''

from fractions import Fraction
a,b=map(int, input().split())
c=6-max(a,b)+1
re=Fraction(c,6)
if re==1:
    print(str(re)+'/1')
else:
    print(re)