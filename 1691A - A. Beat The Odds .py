'''

1691A - A. Beat The Odds

'''

for i in range(int(input())):
    a=int(input())
    arr=[int(i) for i in input().split()]
    even=0
    odd=0
    for i in arr:
        if(i%2==0):
            even=even+1
        else:
            odd=odd+1
    print(min(even,odd))