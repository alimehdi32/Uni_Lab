'''
copy content of file
'''
print("Ali Mehdi - 24BCS008")
with open("9April2026/text.txt","r") as file:
    content=file.read()
    with open("9April2026/file.txt", "w") as f:
        f.write(content)
        print("Content copied successfully.")
        f.close()
    file.close()

