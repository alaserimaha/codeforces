'''
25A - A. IQ test

'''

Copy
a=input()
b=[int(b) for b in input().split()]
even_count, odd_count = 0, 0
for num in b:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
         
if even_count> odd_count:
    for i in b:
        if(i%2==1):
            print(b.index(i)+1)
else:
    for i in b:
        if(i%2==0):
            print(b.index(i)+1)