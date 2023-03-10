'''
141A - A. Amusing Joke

'''
a=input()
b=input()
c=input()
ab=[]
newc=[]
for i in a:
    ab.append(i)
for i in b:
    ab.append(i)
for i in c:
    newc.append(i) 
    
for i in ab[:]:
    if i in newc:
        newc.remove(i)
        ab.remove(i)
if (len(newc)==0 and len(ab)==0 ) :
    print('YES')
else:
    print("NO")