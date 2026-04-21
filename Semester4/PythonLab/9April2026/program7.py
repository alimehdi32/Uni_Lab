'''
count lines words and characters
'''
print("Ali Mehdi - 24BCS008")
lines=0
words=0
chars=0
with open("9April2026/text.txt","r") as file:
    content=file.read()
    lines=len(content.split("\n"))
    print(f"Lines: {lines}")
    words=len(content.split(" "))
    print(f"Words: {words}")
    chars=len(content)
    print(f"Characters: {chars}")
    file.close()

