'''
Write python program that accepts a string from the user and analyzes its content. The program should
count and display the number of vowels, consonants, digits, and spaces present in the string. Consider
both uppercase and lowercase vowels.
'''

string = input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
spaces = 0
for char in string:
    if char in 'aeiou':
        vowels += 1
    elif char in 'bcdfghjklmnpqrstvwxyz':
        consonants += 1
    elif char == ' ':
        spaces += 1
    else:
        digits += 1

print(f"Number of vowels: {vowels}\n Number of consonants: {consonants}\n Number of digits: {digits}\n Number of spaces: {spaces}")