'''
Write a program in python to check whether the input year is a leap year or not.
'''
print("Ali Mehdi - 24BCS008")

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")