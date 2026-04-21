print("Ali Mehdi - 24BCS008")
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

prime_list = []
non_prime_list = []

for num in numbers:
    if num < 2:
        non_prime_list.append(num)
    else:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(num)
        else:
            non_prime_list.append(num)

print("Prime numbers:", prime_list if prime_list else "None")
print("Non-prime numbers:", non_prime_list if non_prime_list else "None")
