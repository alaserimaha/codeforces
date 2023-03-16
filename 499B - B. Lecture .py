'''

499B - B. Lecture


'''

n,m=map(int, input().split())
dic=dict()
for i in range(m):
    a,b=input().split()
    dic[a]=b
re=""    
arr=[(arr) for arr in input().split()]
for i in arr:
    if(len(i)<= len(dic[i])):
        re=re+i+" "
    else:
        re=re+dic[i]+" "
print(re)
        