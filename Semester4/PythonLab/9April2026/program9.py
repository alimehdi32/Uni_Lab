'''
take user input and append data to file
'''

string=input("Enter string to append to file: ")
with open("file.txt", "a") as f:
    f.write(string)
    f.close()

with open("file.txt", "r") as f:
    content=f.read()
    print(content)
    f.close()