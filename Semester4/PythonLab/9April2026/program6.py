'''
open and read content of file
'''

print("Ali Mehdi - 24BCS008")
with open ('9April2026/file.txt','r') as file:
    content=file.read()
    print(content)
    file.close()