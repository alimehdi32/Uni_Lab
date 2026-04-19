'''
open and read content of file
'''

with open ('text.txt','r') as file:
    content=file.read()
    print(content)
    file.close()