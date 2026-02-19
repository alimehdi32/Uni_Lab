# Write a program to take a number as input and check whether a number ends with 4 or 8 and display respectively

print("Ali Mehdi - 24BCS008")
num=int(input("Enter a number: "))
if num%10==4:
    print(f'{num} ends with 4')
elif num%10==8:
    print(f'{num} ends with 8')
else:
    print(f'{num} ends neither with 4 nor with 8')