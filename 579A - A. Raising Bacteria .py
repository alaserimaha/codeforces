'''

579A - A. Raising Bacteria


'''

x = int ( input ( ) )

sol = 0

while x > 0: # 5, 2, 1, 0 then exit
    if x % 2 == 1:
        sol += 1 # 1, 2

    x //= 2 # 2, 1, 0

print(sol) # 2