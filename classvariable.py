#student college system
class student:
    college_name="ABC college"
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    @classmethod
    def change_college(cls,new):
        cls.college_name=new
    @staticmethod
    def is_pass(marks):
        if marks>=35:
            print("pass")
        else:
            print("better luck next time")
    def display(self):
        print("student name:",self.name)
        print("student roll no:",self.roll_no)
        print("college name:",student.college_name)
s1=student("roja",1)
s1.display()
s2=student("anil",2)
s2.display()
s1.change_college("xyz college")
s1.display()
s2.display()
