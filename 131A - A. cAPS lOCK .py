'''
131A - A. cAPS lOCK

'''

a=input()
if(len(a)==1&a.isupper()):
    a=a.lower()
elif(len(a)==1&a.islower()):
    a=a.upper()
elif(a.isupper()):
    a=a.lower()
elif(a[1:].isupper()):
    a=a[0].upper()+a[1:].lower()
print(a)