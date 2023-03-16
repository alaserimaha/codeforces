'''

1335B - B. Construct the String


'''

for i in range(int(input())):
    arr=list("abcdefghijklmnopqrstuvwxyz")
    n,a,b=map(int, input().split())
    litter=[arr[i] for i in range(b)]
    full=""
    i=0;
    while n!=0:
        if(i==b):
            i=0
        full=full+litter[i]
        i=i+1
        n=n-1
    print(full)
        