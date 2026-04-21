print("Ali Mehdi - 24BCS008")
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,18,20]
list2=[]
print(f'list1: {list1}')

for i in range(len(list1)):
    if i<3 and i>17:
        list2.append(list1[i])
    else:
        list2.append(list1[i]+1)

print(f'list2: {list2}')
sum=0
for i in range(len(list2)):
    sum+=list2[i]

print(f'Sum: {sum}')
# list1=[]
# list1[0]=1
# print(list1)