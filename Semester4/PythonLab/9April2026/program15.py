'''
count vowels
'''
print("Ali Mehdi - 24BCS008")
vowels = "aeiou"
freq=0

with open("9April2026/file2.txt","r") as f:
    content=f.read()
    for char in content:
        if char in vowels:
            freq+=1

print(f"{freq} is total vowels present")