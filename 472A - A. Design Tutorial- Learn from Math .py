'''

472A - A. Design Tutorial: Learn from Math


'''

def is_prime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return True
    return False
 
a=int(input())
b=a-4
c=4
while True:
    if is_prime(b) and is_prime(c):
        print(c,b)
        break
    else:
        b=b-1
        c=c+1