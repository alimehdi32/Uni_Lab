print("Ali Mehdi - 24BCS008")
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

count = 0  # Position to place the next non-zero element

for i in range(len(numbers)):
    if numbers[i] != 0:
        numbers[count] = numbers[i]
        count += 1

while count < len(numbers):
    numbers[count] = 0
    count += 1

print("After shifting zeroes to the right:", numbers)
