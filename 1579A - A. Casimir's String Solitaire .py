'''

1579A - A. Casimir's String Solitaire


'''

for i in range(int(input())):
    a=input()
    if(a.count("B")==a.count("A")+a.count("C")):
        print("YES")
    else:
        print("NO")