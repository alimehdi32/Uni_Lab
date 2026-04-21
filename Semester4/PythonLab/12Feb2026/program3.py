# write a program to print all prime numbers  from 100 to 999

print("Ali Mehdi - 24BCS008")

num=100
while(num<=999):
    count=0
    for i in range(1,num+1):
        if(num%i==0):
            count=count+1

    if count==2:
        print(num, end=" ")

    num=num+1

    