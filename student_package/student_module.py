"""Student - attributes/state
• studentRollno
• studentName
• studentMailid
• studentPercentage
• schoolName
• schoolAddress"""

class Student:
    school_name = None
    school_address = None

    def __init__(self,student_name=None ,student_rollno=None ,student_mailid=None ,student_percentange=None):
        self.student_name = student_name
        self.student_rollno = student_rollno
        self.student_mailid = student_mailid
        self.student_percentange = student_percentange

    def get_student_name(self):
        return self.student_name

    #Create a non static method to print - Hi, Peter - Your percentage is 98.5

    @property
    def get_name_with_percentage(self):
        return "Hi " + self.student_name + " your percentage is " + str(self.student_percentange)

    @staticmethod
    def get_school_details():
        return Student.school_name