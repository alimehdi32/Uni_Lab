print("Ali Mehdi - 24BCS008")
test = [3,6,78,45,12,34,65,43,90,87,77,67,49]
print(f'Current list: {test}')

print("Even elements:")
for i in range(len(test)):
    if test[i]%2==0:
        print(test[i])

print("Even position elements")
for i in range(len(test)):
    if i%2==0:
        print(test[i])