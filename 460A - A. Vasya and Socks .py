'''

460A - A. Vasya and Socks


'''

n,m=map(int, input().split())
def cout(total, newtotal):
    new=[n % m == 0 for n in list(range(total+1,newtotal+1))].count(True)
    if new==0 :
        return(newtotal)
    else:
        total=newtotal
        newtotal=newtotal+new
        return(cout(total, newtotal))
print(cout(n,(n+(n//m))))