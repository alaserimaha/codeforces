'''

34B - B. Sale


'''
n,m=map(int , input().split())
arr=[int(arr) for arr in input().split()]
re=[(i*-1) for i in arr if i<0]
re=sorted(re)
print(sum(re[-m:]))