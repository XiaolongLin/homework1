grade1=int[input("Enter your course 1 letter grade: ")]
credit1=int[input("Enter your course 1 credit: ")]
print("Grade point for course 1 is:gradepoint1")
grade2=int[input("Enter your course 2 letter grade: ")]
credit2=int[input("Enter your course 2 credit: ")]
grade3=int[input("Enter your course 3 letter grade: ")]
credit3=int[input("Enter your course 3 credit: ")]
GPA = (gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3)  
print("Your grade is"+GPA)



