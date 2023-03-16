'''

742A - A. Arpa’s hard exam and Mehrdad’s naive cheat


'''

arr=[8,4,2,6]
a=int(input())
if(a==0):
    print(1)
else:
    print(arr[a%4-1])
         