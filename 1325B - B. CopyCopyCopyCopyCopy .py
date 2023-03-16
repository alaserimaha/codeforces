'''

1325B - B. CopyCopyCopyCopyCopy


'''
for i in range(int(input())):
    size=int(input())
    arr=[int(arr) for arr in input().split()]
    arr = list(set(arr))
    print(len(arr))