'''

822A - A. I'm bored with life


'''
import math
a,b=map(int, input().split())
b=math.factorial(min(a,b))
print(b)