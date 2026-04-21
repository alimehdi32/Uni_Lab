'''
search specific word in a file and count how many times it is present
'''
print("Ali Mehdi - 24BCS008")
wordfreq=input("enter the word ")
freq={}
with open("9April2026/file.txt","r") as f:
    content=f.read()
    words=content.split(' ')
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1

print(f"{wordfreq} is present in the file {freq[wordfreq]} times")