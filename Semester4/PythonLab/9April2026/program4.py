'''
Write a program in python that counts the frequency of each character in a given string and displays the result.
'''

string=input("Enter a string: ")
freq={}

for char in string:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1

for key,value in freq.items():
    print(key,":",value)