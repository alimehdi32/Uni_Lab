'''
Write a program in python to implement a dictionary with the following options:
1. Add key value pair
2. search by key
3. search by value
4. update the dict
5. delete the value specified by the user
6. print sorted dictionary

'''

print("Ali Mehdi - 24BCS008")
while True:
    print("1. Add key value pair")
    print("2. Search by key")
    print("3. Search by value")
    print("4. Update dictionary")
    print("5. Delete the value")
    print("6. Print sorted dictionary")
    print("7. Exit")
    dictionary = {}
    option = int(input("Enter your choice: "))
    if option == 1:
        key = input("Enter your key: ")
        value = input("Enter your value: ")
        dictionary[key] = value

    elif option == 2:
        key = input("Enter your key: ")
        print(f"Key: {key} Value: {dictionary[key]}")

    elif option == 3:
        val=input("Enter your value: ")
        for key,value in dictionary.items():
            if val==value:
                print(f"{key}: {value}")

    elif option == 4:
        key=input("Enter your key to be updated: ")
        dictionary[key]=input("Enter your value: ")

    elif option == 5:
        val=input("Enter your value: ")
        for key,value in dictionary.items():
            if val==value:
                del dictionary[key]

    elif option == 6:
        sorted_dict=sorted(dictionary.items())
        print(sorted_dict)

    else:
        break
