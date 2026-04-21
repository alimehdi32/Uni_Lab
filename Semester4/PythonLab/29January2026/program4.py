'''
Write a program in python to calculate train ticket price with discount.
'''
print("Ali Mehdi - 24BCS008")

distance = float(input("Enter distance: "))
base_price = float(input("Enter base price: "))
choice = input("Enter class (AC/Non-AC): ")
category = input("Enter category (Student/Senior/Normal): ")

if choice == "AC":
    price = base_price * 3 * distance
else:
    price = base_price * 2 * distance

if category == "Student" or category == "Senior":
    price = price * 0.9

print("Total Ticket Price:", price)