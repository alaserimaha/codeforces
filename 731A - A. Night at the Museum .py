'''

731A - A. Night at the Museum

'''
arr=list(map(chr, range(97, 123)))
a=input()
pointer=0
total=0
for i in a:
    total=total+min(abs(arr.index(i)-pointer),abs(26-arr.index(i)+pointer) ,abs(26-pointer+arr.index(i)))
    pointer=arr.index(i)    
print(total)       