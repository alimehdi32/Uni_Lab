'''
replace all occurences of specified word with another word and save in new file
'''

content=""
rmword=input("Enter a word to be replaced")
rpword=input("Enter another word to replace")
with open("text.txt","r") as f:
    string=f.read().split(" ")
    for word in string:
        if word==rmword:
            content=content+rpword
        else:
            content=content+word

with open("file3.txt","w") as f:
    f.write(content)
