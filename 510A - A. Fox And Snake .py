'''
510A - A. Fox And Snake

'''
a,b=input().split()
a=int(a)
b=int(b)
bool=True
for i in range(a):
    if i%2==0:
        for c in range(b):
            if(c==b-1):
                print("#") 
            else:
                print("#",end="")
    elif(i%2==1):
        for c in range(b):
            if(bool==True):
                if c==b-1:
                    print("#")
                else:
                    print(".",end="")
            elif(bool==False):
                if c==0:
                    print("#",end="")
                elif(c==b-1):
                    print(".")
                else:
                    print(".",end="")
                
    if (i%2==1):
        bool=not bool