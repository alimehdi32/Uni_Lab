'''
Write a program in python to read a file and handle the exception if the file does not exist.
'''
print("Ali Mehdi - 24BCS008")

filename = input("Enter the file name: ")

try:
    file = open(filename, "r")
    content = file.read()
    print("File Content:\n", content)
    file.close()
except FileNotFoundError:
    print("Error: File does not exist.")