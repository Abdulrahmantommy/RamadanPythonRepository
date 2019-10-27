
totalMarks = 0
numberOfStudents = 0
marks = int(input("Enter the marks of students or a negative value to quit: "))
while marks >=0:
    totalMarks += marks
    numberOfStudents += 1
    marks = int(input())
print("The total number of students is: {}".format(numberOfStudents))
print("The total marks of students is : {}".format(totalMarks))
print("The average mark of students is: {:.2f}".format(totalMarks/numberOfStudents))

    















