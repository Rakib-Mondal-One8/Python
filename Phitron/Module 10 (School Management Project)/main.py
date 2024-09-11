from school import School
from person import Student
from person import Teacher
from subject import  Subject
from classroom import ClassRoom

school = School("ABC","Kolkata")
eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

# Adding student
rakib = Student("Rakib",ten)
rajesh = Student("rajesh",ten)
fahim = Student('fahim',ten)
rohit = Student('rohit',ten)

school.student_admission(rakib)
school.student_admission(rajesh)
school.student_admission(rohit)
school.student_admission(fahim)

# adding teachers
abul = Teacher("Abul Khan")
babul = Teacher('Babul Khan')
kabul = Teacher('Kabul Khan')

# Adding Subject
bangla = Subject("Bangla",abul)
physics = Subject("Physics",babul)
bio = Subject("Bio",kabul)

school.add_teacher(bangla,abul)
school.add_teacher(physics,babul)
school.add_teacher(bio,kabul)

ten.add_subject(physics)
ten.add_subject(bangla)
ten.add_subject(bio)

ten.take_semester()
print(school)
