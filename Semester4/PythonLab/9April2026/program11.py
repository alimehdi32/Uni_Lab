'''
convert all content to uppercase and write into new file
'''
print("Ali Mehdi - 24BCS008")
with open('9April2026/text.txt','r') as f:
    content=f.read().upper()
    with open('9April2026/file1.txt','w') as file:
        file.write(content)
        print("Content converted to uppercase and written to file1.txt successfully.")

