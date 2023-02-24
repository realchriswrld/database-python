from  main import Student

try:

    student_name = input("Enter name \n")
    student_age = input("Enter age \n")
    student_verification = input("Enter verification \n")
    student_stream = input("Enter stream \n")
    student_gender = input("Enter gender \n")

    Student.create( name = student_name, age = student_age,  verfication = student_verification, stream = student_stream, gender = student_gender)
    print("Student created successfully")


except:
    print("failed to create student give enough details")
