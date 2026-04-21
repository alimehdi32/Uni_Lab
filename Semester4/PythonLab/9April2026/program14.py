'''
replace all occurences of specified word with another word and save in new file
'''
print("Ali Mehdi - 24BCS008")
content=""
rmword=input("Enter a word to be replaced")
rpword=input("Enter another word to replace")
with open("9April2026/text.txt","r") as f:
    string=f.read().split(" ")
    for word in string:
        if word==rmword:
            content=content+rpword
        else:
            content=content+word

with open("9April2026/file3.txt","w") as f:
    f.write(content)
