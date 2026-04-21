'''
Write a python program that takes a sentence as input and reverses each word individually while maintaining the original word order.
'''
print("Ali Mehdi - 24BCS008")
string = input("Enter a sentence: ")
stri = string.split(' ')
nwstr=""
for word in stri:
    wrd=""
    for char in word:
        wrd=char+wrd
    nwstr=nwstr+" "+wrd

print(nwstr)