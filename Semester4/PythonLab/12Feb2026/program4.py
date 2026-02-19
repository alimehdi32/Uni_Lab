# Write a program to print Armstrong numbers from 100 to 999

print("Ali Mehdi - 24BCS008")

num=100
while(num<=999):
    power = 0
    temp = num
    while (temp != 0):
        power = power + 1
        temp = temp // 10

    temp = num
    newNum = 0
    while (temp != 0):
        digit = temp % 10
        tempPower = power - 1
        for i in range(tempPower):
            digit = digit * digit

        newNum = newNum + digit
        temp = temp // 10

    if newNum == num:
        print(num)
    #num=num+1
