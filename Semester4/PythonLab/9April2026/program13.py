'''
find the longest word in the file
'''
lonstr=""
with open('text.txt','r') as f:
    longest=0
    string = f.read().split(' ')
    for word in string:
        if longest<len(word):
            longest=len(word)
            lonstr=word

print(f"{lonstr} is present in the file")