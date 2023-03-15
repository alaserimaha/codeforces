'''

492A - A. Vanya and Cubes

'''

a=int(input())-1
count=1
total=1
i=2
while a>0:
    if(total+i<=a):
        count=count+1
        total=total+i
        a=a-total
        i=i+1
    else:
        break
print(count)