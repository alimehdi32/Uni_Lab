print("Ali Mehdi - 24BCS008")

filename = input("Enter the file name: ")
data = input("Enter data to append: ")

try:
    file = open(filename, "a")
    file.write(data)
    print("Data appended successfully.")
    file.close()
except Exception as e:
    print("An error occurred:", e)