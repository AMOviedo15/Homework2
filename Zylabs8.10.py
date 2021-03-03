#Aaron Oviedo #1990958

userval = input()
i = 0
j = len(userval)-1
result = True
while(i<j):
    if(userval[i]==' '):
        i+=1
    elif(userval[j]==' '):
        j-=1
    elif(userval[i]!=userval[j]):
        result = False
        break
    else:
        i+=1
        j-=1
if (result):
    print(userval,"is a palindrome")
else:
    print(userval, "is not a palindrome")