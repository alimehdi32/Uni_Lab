'''
Write a program in python to find roots of a quadratic equation.
'''
print("Ali Mehdi - 24BCS008")

import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = b*b - 4*a*c

if d > 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print("Roots are real and different:", r1, r2)
elif d == 0:
    r = -b / (2*a)
    print("Roots are real and same:", r)
else:
    print("Roots are complex")