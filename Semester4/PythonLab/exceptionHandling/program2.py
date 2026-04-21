'''
Write a program in python to write data into a file and handle exceptions if permission is denied.
'''
print("Ali Mehdi - 24BCS008")

filename = input("Enter the file name: ")
data = input("Enter data to write: ")

try:
    file = open(filename, "w")
    file.write(data)
    print("Data written successfully.")
    file.close()
except PermissionError:
    print("Error: Permission denied.")