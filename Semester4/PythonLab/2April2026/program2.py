'''
write a program in python to repeatedly ask the user to input student names and their score in 3 subjects and store that in a dict as key value pair
then perform
1. Program should ask the user name and display their percentage
2. Generate a list of students who secure more than 75%
3. Find the student name with highest mark in every subject
'''




print("Ali Mehdi - 24BCS008")
score={}

while True:
    choice=input("Enter score Yes/No: ")
    if choice == "No":
        break
    name=input("Student name: ")
    m1=int(input("Marks in English: "))
    m2=int(input("Marks in Maths: "))
    m3=int(input("Marks in Science: "))

    score[name]=[m1,m2,m3]

perc_score={}
students75=[]

for key,value in score.items():
    mark_english = score[key][0]
    mark_maths = score[key][1]
    mark_science = score[key][2]
    percentage = (mark_english + mark_maths + mark_science) / 3
    perc_score[key]=percentage
    if percentage > 75:
        students75.append(key)

username=input("Enter Student Name to get percentage: ")
print(perc_score[username])
print(f"List of Students who secured more than 75%: {students75}")

subjects=3
sub={
    0: "English",
    1: "Maths",
    2: "Science",
}
for i in range(subjects):
    topper=max(score, key= lambda sname: score[sname][i])
    print(f"{sub[i]}: {topper}")



