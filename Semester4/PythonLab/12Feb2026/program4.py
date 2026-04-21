# Write a program to print Armstrong numbers from 100 to 999

print("Ali Mehdi - 24BCS008")

for num in range(100, 1000):
    
    d1 = num // 100           
    d2 = (num // 10) % 10     
    d3 = num % 10             

    
    if num == d1**3 + d2**3 + d3**3:
        print(num, end=" ")

print()  