'''

550A - A. Two Substrings


'''
a=input()
count1t1=a.count("AB")
t1=a.replace("AB"," ",1)
count2t1=t1.count("BA")

count1t2=a.count("BA")
t2=a.replace("BA"," ",1)
count2t2=t2.count("AB")
if((count1t1>=1 and count2t1>=1 )or( count1t2>=1 and count2t2>=1 )):
    print("YES")
else:
    print("NO")