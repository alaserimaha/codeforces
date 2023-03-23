'''
265A - A. Colorful Stones (Simplified Edition)

'''

a=input()
b=input()
i=0
for j in b:
    if(a[i]==j):
        i=i+1
print(i+1)