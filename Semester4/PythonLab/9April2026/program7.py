'''
count lines words and characters
'''
lines=0
words=0
chars=0
with open("text.txt","r") as file:
    content=file.read()
    lines=len(content.split("\n"))
    print(f"Lines: {lines}")
    words=len(content.split(" "))
    print(f"Words: {words}")
    chars=len(content)
    print(f"Characters: {chars}")
    file.close()

