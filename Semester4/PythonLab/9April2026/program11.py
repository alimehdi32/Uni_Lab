'''
convert all content to uppercase and write into new file
'''

with open('text.txt','r') as f:
    content=f.read().upper()
    with open('file1.txt','w') as file:
        file.write(content)

