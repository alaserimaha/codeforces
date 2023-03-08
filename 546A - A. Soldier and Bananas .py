'''
546A - A. Soldier and Bananas
 
'''
a,b,c= input().split()
a,b,c=int(a),int(b),int(c)
total=0;
for i in range(c):
    total=total+((i+1)*a)
still=total -b
if still >=0:
    print(still)
else:
    print(0)