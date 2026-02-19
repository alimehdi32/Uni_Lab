# Write a program to do following: read an int x, determine number of digits in x. Now form a new num y as number of digits in x as tenth place, most significant bit of x at oes place
x=int(input("Enter a number"))
significant=0
digits=0
while(x!=0):
    significant=x%10
    digits=digits+1
    x=x//10

y=digits*10+significant
print(y)