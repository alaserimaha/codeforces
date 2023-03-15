'''

474A - A. Keyboard

'''
st="qwertyuiop asdfghjkl; zxcvbnm,./"
a=input()
word=input()
new=""
if a=='R':
    for i in word:
        new=new+st[st.index(i)-1]
    print(new)
else:
    for i in word:
        new=new+st[st.index(i)+1]
    print(new)