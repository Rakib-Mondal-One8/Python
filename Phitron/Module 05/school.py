"""
class Student:
    def __init__(self,name,cur_class,id):
        self.name = name
        self.cur_class = cur_class
        self.id = id
    def __repr__(self) ->str:
        return f'{self.name} {self.cur_class} {self.id}'

class Teacher:
    def __init__(self,name,subject,id):
        self.name = name
        self.subject = subject
        self.id = id
    def __repr__(self) ->str:
        return f'{self.name} {self.subject} {self.id}'


alia = Student('alia bhat',9,1234)
ranbeer = Teacher('ranbeer',"Algorithm",1234)
print(alia)
print(ranbeer)
"""

class School:
    def __init__(self,name):
        self.name = name
        self.teacher = []
        self.students = []
    def add_teacher(self,name,subject):
        id = len(self.teacher)+1
        teacher = (name,subject,id)
        self.teacher.append(teacher)

    def enroll(self,name,fee):
        if fee<6500:
            print("Not enough")
        else:
            id = len(self.students)+1
            student = (name,'C',id)
            self.students.append(student)
            print("Congratulations you are Enrolled , your id is", id)
    def __repr__(self) -> str:
        print("Welcome to ",self.name)
        print("----------our Teachers----------")
        for t in self.teacher:
            print(t)
        print("-----------our students----------")
        for s in self.students:
            print(s)
        return "All done"


phitron = School('phitron')
phitron.enroll('Rakib',6500)
phitron.enroll('Rohit',7000)
phitron.enroll('Robert',50000000)
phitron.add_teacher('Tom cruise','c')
phitron.add_teacher('Shah Rukh Khan','c++')
phitron.add_teacher('Robert downey Jr','python')
print(phitron)
