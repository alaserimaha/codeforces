'''
894A - A. QAQ

'''

s=input()
q=[i for i in range(len(s)) if s[i]=='Q']
if(len(q)<2):
    print(0)
else:
    a=[i for i in range(len(s)) if s[i]=='A' and q[0]<i<q[-1]]
    if(len(a)<1):
        print(0)
    else:
        count=0
        temp=-1
        for i in q:
            for j in a:
                while True:
                    if(i<j<q[temp]):
                        count=count+1
                        temp=temp-1
                    else:
                        break
                temp=-1
        print(count)