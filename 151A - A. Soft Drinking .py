'''
151A - A. Soft Drinking


'''
arr=[int(arr) for arr in input().split()]
n, k, l, c, d, p, nl, np=arr
num1=k*l/nl
num2=c*d
num3=p/np
print(int(min(num1,num2,num3)/n))