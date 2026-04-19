'''
Write a python program to remove duplicate characters from a string while preserving the original order.
'''

string=input("Enter a string: ")
freq={}

for char in string:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1

str1=""
for key,value in freq.items():
    str1=str1+key

print(str1)