'''
remove punctuation from (.? etc) and add cleaned text to another file
'''

print("Ali Mehdi - 24BCS008")
string=""
with open("9April2026/text.txt","r") as f:
    text=f.read()

    for char in text:
        if char in ".!?@#$%^&*()_-":
            continue
        else:
            string+=char


with open("9April2026/file2.txt","w") as f:
    f.write(string)
    print("Punctuation removed and cleaned text written to file2.txt successfully.")
