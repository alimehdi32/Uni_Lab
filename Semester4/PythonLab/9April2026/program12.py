'''
remove punctuation from (.? etc) and add cleaned text to another file
'''
string=""
with open("text.txt","r") as f:
    text=f.read()

    for char in text:
        if char in ".!?@#$%^&*()_-":
            continue
        else:
            string+=char


with open("file2.txt","w") as f:
    f.write(string)
