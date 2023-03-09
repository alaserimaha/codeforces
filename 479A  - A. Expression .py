'''
479A  - A. Expression

'''
a=int(input())
b=int(input())
c=int(input())
 
d=[a*b*c,a+b+c,a*b+c,a+b*c,(a+b)*c, a*(b+c)]
print(max(d))