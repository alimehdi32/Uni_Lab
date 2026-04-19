'''
search specific word in a file and count how many times it is present
'''

word=input("enter the word")
freq={}
with open("file.txt","r") as f:
    content=f.read()
    words=content.split(' ')
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1

print(f"{word} is present in the file {freq[word]} times")