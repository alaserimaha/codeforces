'''

379A - A. New Year Candles


'''

def count(a,b,total):
    if(b>a):
        return(total)
    else:
        total=total+a//b
        a=a//b +(a-(a//b*b))
        return(count(a,b,total))
a,b=map(int , input().split())
print(count(a,b,a))