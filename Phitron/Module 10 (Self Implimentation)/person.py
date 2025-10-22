class Person:
    def __init__(self,name):
        self.name = name


class Teacher(Person):
    def __init__(self,name):
        super().__init__(name)

    def teach(self):
        pass
    def evaluate_exam(self):
        pass


class Student(Person):
    def __init__(self,name,classroom):
        super().__init__(name)
        self.classroom = classroom
        self.marks = {}
        self.subject_grade = {}
        self.grade = None
        self.__id = None

    def calculate_final_grade(self):
        pass

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,value):
        if(self.classroom.id_exists(value) == False):
            self.__id = value
        else:
            print("Sorry !! Student with similar ID already Exists!!")
