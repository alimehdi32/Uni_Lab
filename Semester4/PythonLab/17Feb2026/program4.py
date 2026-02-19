list1=[1,1,1,2,2,8,5,5,7,7,7,7,3,3,3,4,9]
k=int(input("Enter K:"))
done=[]
for i in range(len(list1)):
    if list1[i] in done:
        continue
    else:
        freq=0
        for j in range(len(list1)):
            if list1[j]==list1[i]:
                freq+=1
        
        if freq>k:
            print(f'{list1[i]}: {freq}')
            
        done.append(list1[i])

