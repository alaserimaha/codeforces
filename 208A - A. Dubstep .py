'''
208A - A. Dubstep

'''

phrase = input()
substituted_phrase = phrase.replace("WUB", " " )
while True:
    if(substituted_phrase[0]==" "):
        substituted_phrase=substituted_phrase[1:]
    else:
        break
while True:
    if(substituted_phrase[len(substituted_phrase)-1]==" "):
        substituted_phrase=substituted_phrase[:-1]
    else:
        break
substituted_phrase = substituted_phrase.replace("  ", " " )
 
print(substituted_phrase)
