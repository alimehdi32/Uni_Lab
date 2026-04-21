'''
Write a python program to check whether a given string is a palindrome. Ignore case differences and spaces while checking.
'''
print("Ali Mehdi - 24BCS008")
string=input("Enter a string: ")
nwstr=string.lower().split(' ')
strr=""
for word in nwstr:
    strr=strr+word

str1=""
for char in strr:
    str1=char+str1

if str1==strr:
    print("Yes")
else:
    print("No")