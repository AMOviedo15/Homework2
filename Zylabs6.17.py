#Aaron Oviedo #1990958

i = 0
userpass = input()
newpass = ""

while i  < len(userpass):
    index = userpass[i]
    if index == 'i':
        newpass += '!'
    elif index == 'a':
        newpass += '@'
    elif index == 'm':
        newpass += 'M'
    elif index == 'B':
        newpass += '8'
    elif index == 'o':
        newpass += '.'
    else:
        newpass += index
    i += 1
newpass += "q*s"

print(newpass)