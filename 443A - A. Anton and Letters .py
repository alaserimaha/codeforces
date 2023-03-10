'''
443A - A. Anton and Letters

'''

a=input()[1:-1]
a=a.replace(" ","")
a=a.replace(",","")
 
b=[]
count=0;
for i in a:
    if i not in b:
        count=count+1
        b.append(i)
        
 
print(count)