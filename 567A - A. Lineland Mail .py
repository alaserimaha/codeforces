'''

567A - A. Lineland Mail

'''
a=int(input())
arr=[int(i) for i in input().split()]
for i in range(a):
    if(i==0):
        print(abs(arr[i]-arr[i+1]), abs(arr[-1]-arr[i]))
    elif(i==a-1):
        print(abs(arr[i]-arr[-2]), abs(arr[i]-arr[0]))
    else:
        print(abs(min(arr[i]-arr[i-1], arr[i+1]-arr[i])), abs(max(arr[i]-arr[0], arr[-1]-arr[i])))