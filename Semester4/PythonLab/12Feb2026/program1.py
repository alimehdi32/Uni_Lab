# Write a program that takes positive numbers as input and do following operations:
# 1. if number of digits is even print sum of digits
# 2. if number of digits is odd then program should move to next iteration
# 3. The program should terminate if number is negative
# 4. Print total number of iterations

print("Ali Mehdi - 24BCS008")

num=int(input("Enter number: "))
count=0
if num<0:
    print("Sorry, the number can't be less than zero.")
    exit()

sum_even=0
while num>0:
    digit=num%10
    count=count+1
    sum_even=sum_even+digit
    num=num//10

if count%2==0:
    print(f'Sum of digits is: {sum_even}')

print(f'Total iterations performed: {count}')