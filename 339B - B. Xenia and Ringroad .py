'''
339B - B. Xenia and Ringroad

'''
a,b=input().split()
a=int(a)
b=int(b)
arr=[int(arr) for arr in input().split()]
current=1
time=0
for i in arr:
    if(current<i):
        time=time+(i-current)
        current=i
    elif(current>i):
        time=time+(a-current)+i
        current=i
print(time)