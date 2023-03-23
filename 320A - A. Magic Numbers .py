'''
320A - A. Magic Numbers

'''
a=input()
a=a.replace('144', ' ')
a=a.replace('14', ' ')
a=a.replace('1', ' ' )
a=a.replace(' ', '' )

if(len(a)>0):
    print('NO')
else:
    print("YES")