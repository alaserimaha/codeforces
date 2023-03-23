'''

1535B - B. Array Reodering

'''
import math
for _ in range(int(input())):
  n=int(input())
  l=list(map(int,input().split()))
  c=0
  for i in range(n-1):
    for j in range(i+1,n):
      if(math.gcd(l[i],2*l[j])>1 or math.gcd(2*l[i],l[j])>1):
        c+=1
  print(c)