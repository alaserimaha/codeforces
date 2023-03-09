'''
122A - A. Lucky Division

'''

arr=[4,7,47,74,477,444,474,777,747,744]
a=int(input())
re="NO"
for i in arr:
    if(a%i==0):
        re="YES"
        break
print(re)