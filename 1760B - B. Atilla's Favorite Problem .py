'''

1760B - B. Atilla's Favorite Problem


'''
arr=list('abcdefghijklmnopqrstuvwxyz')
for i in range(int(input())):
    a=int(input())
    n=list(input())
    print(arr.index(max(n))+1)