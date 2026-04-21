'''
Write a program in python to input three numbers and print them in ascending order.
'''
'''
Write a program in python to input three numbers and print them in ascending order without using built-in functions.
'''
print("Ali Mehdi - 24BCS008")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Manual sorting using conditions
if a <= b and a <= c:
    if b <= c:
        print("Ascending order:", a, b, c)
    else:
        print("Ascending order:", a, c, b)

elif b <= a and b <= c:
    if a <= c:
        print("Ascending order:", b, a, c)
    else:
        print("Ascending order:", b, c, a)

else:
    if a <= b:
        print("Ascending order:", c, a, b)
    else:
        print("Ascending order:", c, b, a)