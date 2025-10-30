class ClassRoom:
    def __init__(self,name):
        self.name = name
        self.students = []
        self.subjects = []

    def add_student(self,student):
        self.students.append(student)
        print(f'New Student Added in class {self.name}')

    def add_subject(self,subject):
        pass
    def take_semester_final(self):
        pass
    def get_top_students(self):
        pass

    def id_exists(self,value):
        for student in self.students:
            if(value == student.id()):
                return True
            else:
                return False

    def generate_id(self):
        cnt = len(self.students)+1
        return cnt

    def __repr__(self):
        return (f"{self.name}: {[subject.name for subject in self.subjects]}")