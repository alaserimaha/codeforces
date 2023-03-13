'''

1343A - A. Candies


'''

for i in range(int(input())):
	n=int(input())
	b=3
	j=3
	while n%b!=0:
		b=2**j-1
		j+=1
	print(n//b)