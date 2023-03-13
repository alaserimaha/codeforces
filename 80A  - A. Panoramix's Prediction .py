'''

80A	 - A. Panoramix's Prediction


'''
def isPrime(Number):
    return 2 in [Number,2**Number%Number]
a,b=map(int, input().split())
if (isPrime(a) == False or isPrime(b)==False) :
    print('NO')
else:
    re="YES"
    for i in range(a+1,b):
        if(isPrime(i)):
            re="NO"
            break
    print(re)