count=0
highest=0
sechighest=0
while(count<10):
    num=int(input("Enter a number: "))
    if(num>highest):
        highest=num
    if(sechighest<num):
        sechighest=num
    count=count+1

print(f'The highest number is: {highest}  & second highest number is: {sechighest}')