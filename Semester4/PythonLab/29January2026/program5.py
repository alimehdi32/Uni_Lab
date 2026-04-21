'''
Write a program in python to perform operations on three numbers based on conditions.
'''
print("Ali Mehdi - 24BCS008")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a != b and b != c and a != c:
    print("Sum:", a + b + c)
elif a == b == c:
    print("0")
elif a == b or a == c:
    print(a)
else:
    print(b)