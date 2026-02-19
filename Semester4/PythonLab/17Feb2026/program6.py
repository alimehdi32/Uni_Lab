list1=[1,1,1,2,2,8,5,5,7,7,7,7,3,3,3,4,9]
print(f'list1: {list1}')

list2=[]
k=int(input("Enter number of rotations:"))
pos=len(list1)-1
while k>0:
    list2.insert(0,list1[pos])
    pos-=1
    k-=1

for i in range(0,pos+1):
    list2.append(list1[i])

print(f'Rotated list: {list2}')
