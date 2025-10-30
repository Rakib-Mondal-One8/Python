import random

from classroom import *
from subject import *
from person import *

#--------------------------------------------------------------------------------------------------------------------#

class School:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.teachers = []
        self.classrooms = {}

    def add_classroom(self,classroom): # classroom object
        self.classrooms[classroom.name] = classroom

    def add_teacher(self,subject,teacher):
        self.teachers.append(teacher)
        subject.teachers.append(teacher)
        print('Teacher added!!')

    def student_admission(self,name,class_name):
        classroom = self.classrooms[class_name]
        s = Student(name,classroom)
        s.id = classroom.generate_id()
        classroom.add_subject(s)

        print("Student Admitted!!")
        print(f"Student ID: {s.id}")

    def calculate_grade(self,marks):
        pass

    def grade_to_value(self):
        pass
    def value_to_grade(self):
        pass

    def __repr__(self):
        print(f'***** Welcome to {self.name} *****')
        print(f"***** Our Faculties *****")
        for teacher in self.teachers:
             return f"{teacher}: {[subject.name for subject in teacher.subject]}"

        print(f"***** Our Classrooms *****")
        for classroom in self.classrooms.values():
            print(classroom)



# sub = Subject('Physics')
# inst = Teacher('Sufiyan Alam',sub)
# sub2 = Subject('Math')
# inst.add_subject(sub2)
# Sch = School('Heritage','Kolkata')
# Sch.add_teacher(sub,inst)
# print(Sch)




