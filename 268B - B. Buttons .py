'''

268B - B. Buttons

'''
a=int(input())
count=0
j=1
arr=[]
for i in range(a-1):
    count=count+j
    j=j+1
    arr.append(count)
print(sum(arr)+a)