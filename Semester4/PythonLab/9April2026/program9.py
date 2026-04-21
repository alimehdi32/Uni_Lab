'''
take user input and append data to file
'''
print("Ali Mehdi - 24BCS008")
string=input("Enter string to append to file: ")
with open("9April2026/file.txt", "a") as f:
    f.write(string)
    f.close()

with open("9April2026/file.txt", "r") as f:
    content=f.read()
    print(content)
    f.close()