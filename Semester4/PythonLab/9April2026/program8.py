'''
copy content of file
'''

with open("text.txt","r") as file:
    content=file.read()
    with open("file.txt", "w") as f:
        f.write(content)
        f.close()
    file.close()

