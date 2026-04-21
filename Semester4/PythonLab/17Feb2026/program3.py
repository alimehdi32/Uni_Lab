
print("Ali Mehdi - 24BCS008")
lst = []

while True:
    print("\n--- Menu ---")
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Insert at particular position")
    print("4. Delete at beginning")
    print("5. Delete at end")
    print("6. Delete at particular position")
    print("7. Search a particular element")
    print("8. Reverse the list")
    print("9. Display list")
    print("0. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        lst.insert(0, value)

    elif choice == 2:
        value = int(input("Enter value: "))
        lst.append(value)

    elif choice == 3:
        value = int(input("Enter value: "))
        pos = int(input("Enter position (1-based): "))
        if 1 <= pos <= len(lst) + 1:
            lst.insert(pos - 1, value)
        else:
            print("Invalid position.")

    elif choice == 4:
        if lst:
            lst.pop(0)
        else:
            print("List is empty.")

    elif choice == 5:
        if lst:
            lst.pop()
        else:
            print("List is empty.")

    elif choice == 6:
        pos = int(input("Enter position (1-based): "))
        if 1 <= pos <= len(lst):
            lst.pop(pos - 1)
        else:
            print("Invalid position.")

    elif choice == 7:
        value = int(input("Enter value to search: "))
        if value in lst:
            print(f"Element {value} found at position {lst.index(value) + 1}")
        else:
            print("Element not found.")

    elif choice == 8:
        lst.reverse()

    elif choice == 9:
        print("List:", lst if lst else "Empty")

    elif choice == 0:
        break

    else:
        print("Invalid choice.")

    print("Current List:", lst if lst else "Empty")
