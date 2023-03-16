'''

509A - A. Maximum in Table


'''

a=int(input())
def cal(a,b):
    if(a==0):
        return(1)
    elif(b==0):
        return(1)
    else:
        return(cal(a-1,b)+cal(a,b-1))
print(cal(a-1,a-1))