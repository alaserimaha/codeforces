'''

556A - A. Case of the Zeros and Ones


'''

a=int(input())
string=input()
print(a-(min(string.count("1"),string.count("0"))*2))