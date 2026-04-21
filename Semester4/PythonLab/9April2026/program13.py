'''
find the longest word in the file
'''
print("Ali Mehdi - 24BCS008")   
lonstr=""
with open('9April2026/text.txt','r') as f:
    longest=0
    string = f.read().split(' ')
    for word in string:
        if longest<len(word):
            longest=len(word)
            lonstr=word

print(f"{lonstr} is present in the file")