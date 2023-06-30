#create a marksheet application for a school
# 3 subjects - maths, science, english
#Student name & marks of 3 subjects
#total marks, if the student has passed or not and grade of student.
#identify the topper from the batch i.e. Highest rank 
#we need to store that information in a variable using list

studentsList = []  #List for students data

flag="y"
while(flag=="y"):  #for storing multiple student's data 
     student = {}  #Dictionary
     studName = input("Please enter the name of student: ")
     student["name"]=studName

     #Taking the inputs for marks
     subjectFlag="y"
     subjectsList =[]   #Subject List

     # taking the inputs for marks
     # validation logic
     totalMarks=0
     while(subjectFlag=="y"):
        subject={}  #Subject Dictionary
        subjectName = (input("Please enter name of Subject: "))
        marks=int(input("Enter the marks of subject: ")) 
        subject["name"]=subjectName
        subject["marks"]=marks
        subjectsList.append(subject)

        totalMarks = totalMarks + marks
        subjectFlag =input("Do you have any other subject data? y/n ")

#Processing the marks
     totalMarksList = []
     student["totalMarks"]=totalMarks
     totalMarksList.append(totalMarks)
     print("Total marks of",studName, ": ",totalMarks)

#calculate percentage
     percentageMarks = (totalMarks/300)*100
     student["percentageMarks"]=percentageMarks
     student["subjects"]=subjectsList
     studentsList.append(student)   #appending the data in list

#checking if studnet is pass or fail
#grade : 0 to 30: F, 30-60: D, 61-80: 
     if(percentageMarks<=30):
          print(studName," is Fail")
          print("Grade: F")
     elif(percentageMarks<=60):
           print(studName,"is PASS")
           print("Grade : C")
     elif(percentageMarks<=80):
          print(studName,"is PASS")
          print("Grade : B")
     elif(percentageMarks>80):
          print(studName,"is PASS")
          print("Grade : A")
     else:
          print("Try Again..")
     flag = input("do you have anyother student data y/n: ")

print(studentsList)

#find maximum percentage using for loop
topper = 0
topperIndex = 0
for index in range(len(studentsList)):
     if studentsList[index]["percentageMarks"] > topperIndex: 
          topper = studentsList[index]
          topperIndex = index
print("The topper is: ", studentsList[topperIndex])

#ranking 

ranks = [1] * len(studentsList)

for i in range(len(studentsList)):   #Nested Loops
     for j in range(len(studentsList)):
          if studentsList[i]["percentageMarks"]  < studentsList[j]["percentageMarks"]:
               ranks[i]+=1

print("Ranking of all students: ")
for a in range(len(studentsList)):
     print("Rank ", ranks[a], ":", studentsList[a]["name"])