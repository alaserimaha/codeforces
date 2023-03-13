'''

749A - A. Bachgold Problem


'''

a=int(input())
if a%2==0:
    print(a//2)
    print(str('2 ')*(a//2))
else:
    print(a//2)
    print(str('2 ')*(a//2-1)+'3')