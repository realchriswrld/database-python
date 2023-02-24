from  main import  Student

our_students = Student.select()
for Student in our_students:
    print(Student.name, Student.age, Student.verfication, Student.stream, Student.gender)