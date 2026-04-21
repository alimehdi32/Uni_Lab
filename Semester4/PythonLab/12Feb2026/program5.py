print("Ali Mehdi - 24BCS008")
highest = None
second_highest = None

print("Enter 10 numbers:")

for i in range(10):
    try:
        num = float(input(f"Number {i+1}: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        exit(1)

    if highest is None or num > highest:
        second_highest = highest
        highest = num
    elif second_highest is None or (num > second_highest and num != highest):
        second_highest = num

if second_highest is None:
    print("All numbers are the same. No distinct second highest.")
else:
    print(f"Highest number: {highest}")
    print(f"Second highest number: {second_highest}")
