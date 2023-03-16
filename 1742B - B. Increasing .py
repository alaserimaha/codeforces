'''

1742B - B. Increasing


'''

for i in range(int(input())):
    t=int(input())
    arr=[int(arr) for arr in input().split()]
    arr2 = list(set(arr))
    if(len(arr)==len(arr2)):
        print("YES")
    else:
        print("NO")