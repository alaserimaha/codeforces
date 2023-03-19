'''

1294C - C. Product of Three Numbers

'''
def findfactors(n):
    arr=[]
    for i in range(2,n):
        if(i*i>n):
            break
        if(n%i==0):
            n=n//i
            arr.append(i)
    if(n!=1):
        arr.append(n)
    return(list(set(arr)))


for i in range(int(input())):
    a=int(input())
    arr=findfactors(a)
    if(len(arr)>=3 ):
        print("YES")
        print(arr[0],arr[1], a//arr[0]//arr[1])       
    else:
        print("NO")