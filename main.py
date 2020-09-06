grade1=int[input("Enter your course 1 letter grade: ")]
credit1=int[input("Enter your course 1 credit: ")]
if(grade1=A):
  gradepoint1=4.0
elif(grade1=A-):
  gradepoint=3.67
elif(grade1=B+):
  gradepoint1=3.33
elif(grade1=B):
  gradepoint1=3.0
elif(grade1=B-):
  gradepoint1=2.67
elif(grade1=C+):
  gradepoint1=2.33
elif(grade1=C):
  gradepoint1=2.0
elif(grade1=D):
  gradepoint1=1.0
else
  gradepoint1=0.0      

print("Grade point for course 1 is:gradepoint1")
grade2=int[input("Enter your course 2 letter grade: ")]
credit2=int[input("Enter your course 2 credit: ")]
grade3=int[input("Enter your course 3 letter grade: ")]
credit3=int[input("Enter your course 3 credit: ")]
GPA = (gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3)  
print("Your grade is"+GPA)



