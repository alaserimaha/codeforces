'''
469A  - A. I Wanna Be the Guy

'''
n=int(input())
arr1=[int(arr) for arr in input().split()]
arr2=[int(arr) for arr in input().split()]
targetList = list(set(arr1[1:]+arr2[1:]))
if(len(targetList)==n):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")