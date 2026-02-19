list1=[12,43,21,56,77,65,45,43]
while True:
    print(f'List: {list1}')
    print("1. Insert at beginning")
    print("2. Insert at the end")
    print("3. Insert at particular position")
    print("4. Delete at beginning")
    print("5. Delete at the end")
    print("6. Delete at particular position")
    print("7. search a particular element")
    print("8. Reverse the list")
    ch=input(int("Enter choice"))

    if ch==1:
        list1[:]=[input(int("Enter value"))]+list1
    elif ch==2:
        list1+=[input(int("Enter value"))]
    elif ch==3:
        
