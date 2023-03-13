'''

520B - B. Two Buttons


'''

a,b=map(int, input().split())
count=0
while a != b:
    if(b>a):
        if(b%2==0):
            b=b//2
            count=count+1
        else:
            b=b+1
            count=count+1
    else:
        b=b+1
        count=count+1

print(count)