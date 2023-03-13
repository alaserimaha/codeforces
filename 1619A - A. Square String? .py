'''

1619A - A. Square String?


'''
for i in range(int(input())):
    temp=input()
    if(len(temp)==1):
        print("NO") 
        continue
    if(temp[:len(temp)//2]==temp[len(temp)//2:]):
        print("YES")
    else:
        print("NO" )