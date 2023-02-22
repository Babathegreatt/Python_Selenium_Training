from student_package.student_module import Student

Student.school_name = "New English School"
Student.school_address = "Satara"

stud1 = Student("jack", 1001, "jack@gmail.com", 45.2)
stud2 = Student(student_name="peter", student_rollno=1002, student_mailid="peter@gmail.com", student_percentange=88.2)
stud3 = Student("mark", 1003, "mark@gmail.com", 56.2)
stud4 = Student(student_percentange=98.2)
stud5 = Student()

# print Mail ID
print(stud1.student_mailid)
print(stud2.student_mailid)
print(stud3.student_mailid)

print(stud2.get_student_name())

#res = stud1.get_name_with_percentage()
#print(res)

print(Student.get_school_details())

res = stud2.get_name_with_percentage
print(res)