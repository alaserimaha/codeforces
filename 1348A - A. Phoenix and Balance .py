'''

1348A - A. Phoenix and Balance

'''
for i in range(int(input())):
    temp=int(input())
    arr=[2**i for i in range(1,temp+1) ]
    print(abs((sum(arr[0:(temp//2)-1])+arr[-1])-(sum(arr[(temp//2-1):-1]))))