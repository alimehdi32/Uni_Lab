'''
Write a program in python to check the type of input character.
'''
print("Ali Mehdi - 24BCS008")

ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase letter")
elif ch.islower():
    print("Lowercase letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")