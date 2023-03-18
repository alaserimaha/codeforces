'''

1353C - C. Board Moves


'''
for i in range(int(input())):
    n=int(input())
    total=n*n-1
    var=8
    i=1
    step=0
    while total>0:
        step=step+var*i
        total=total-var
        var=var+8
        i=i+1
    print(step)
        