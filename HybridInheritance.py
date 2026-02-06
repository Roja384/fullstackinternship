#program for a College Management System using Hybrid Inheritance
class person:
    def __init__(self,name):
        self.name=name
    def display_person(self):
        print("Name:",self.name)
class student(person):
    def __init__(self,sid,name):
        self.sid=sid
        super().__init__(self,name)
    def display_student(self):
        print("student id:",self.sid)
        super().display_person()
class sports_player(person):
    def __init__(self,sports_name,name):
        self.sports_name=sports_name
        person.__init__(self,name)
    def display_sports_player(self):
        print("sports:",self.sports_name)
        super().display_person()
class college_student(student,sports_player):
    def __init__(self,college_name,name,sid,sports_name):
        self.college_name=college_name
        student.__init__(self,sid,name)
        sports_player.__init__(self,sports_name,name)
    def display_college_student(self):
        super().display_student()
        super().display_sports_player()
        print("college name:",self.college_name)

s=college_student("MITT","Roja",42,"running")
s.display_college_student()