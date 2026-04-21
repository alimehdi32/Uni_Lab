print("Ali Mehdi - 24BCS008")
list1=[1,1,1,2,2,8,5,5,7,7,7,7,3,3,3,4,9]
unique=[]
duplicate=[]
done=[]

for i in range(len(list1)):
    if list1[i] in done:
        continue
    else:
        freq=0
        for j in range(len(list1)):
            if list1[i]==list1[j]:
                freq+=1

        print(f'{list1[i]}: {freq}')
        done.append(list1[i])
        if freq==1:
            unique.append(list1[i])
        else:
            duplicate.append(list1[i])

print(f'Unique: {unique}')
print(f'Duplicate: {duplicate}')