'''
1692B - B. All Distinct

'''

for i in range(int(input())):
    input()
    arr=[int(i) for i in input().split()]
    arr2 = list(set(arr))
    if(len(arr)==len(arr2)):
        print(len(arr))
    elif((len(arr)-len(arr2))%2==0):
        print(len(arr2))
    elif((len(arr)-len(arr2))%2==1):
        print(len(arr2)-1)   
        