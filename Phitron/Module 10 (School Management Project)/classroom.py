class ClassRoom:
    def __init__(self,name):
        self.name = name
        self.students = [] # list of Student Obj
        self.subjects = [] # List of Subject Obj
    def add_student(self,student): # rahim,eight e vorti hobe
        roll_no = f"{self.name}-{len(self.subjects)+1}" # eight - 2
        student.id = roll_no
        self.students.append(student)
    def add_subject(self,subject):
        self.subjects.append(subject)
    def take_semester(self):
        for subject in self.subjects:
            subject.exam(self.students)
        for student in self.students:
            student.calculate_final_grade()