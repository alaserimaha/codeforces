'''

432A - A. Choosing Teams

'''


a,b=input().split()
a=int(a)
b=int(b)
arr=[int(arr) for arr in input().split()]
arr.sort()
count=0
for i in arr:
    if(i+b<=5):
        count=count+1
    else:
        break
if (count%3!=0 and count>=3):
    re=(count//3)
else:
     re=int(count/3)
    
 
print(re)