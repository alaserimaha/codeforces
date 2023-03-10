'''
732A - A. Buy a Shovel

'''
k,r=map(int, input().split())
s=int(k)
total=1
while(s%10!=0 and str(s)[-1]!=str(r) ):
    s=s+k
    total=total+1
print(total)