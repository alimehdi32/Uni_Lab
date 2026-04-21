'''
Write a program in python to display category of a person based on age.
'''
print("Ali Mehdi - 24BCS008")

age = int(input("Enter age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Young")
else:
    print("Adult")