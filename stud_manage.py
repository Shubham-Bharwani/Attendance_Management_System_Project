from login_func import set_student_password
def add_student(users,students, attendance_records,roll_number, name):
    if roll_number in students:
        print("Roll number already exists.")
    else:
        students[roll_number] = name
        attendance_records[roll_number] = {}
        password = input("Enter a password for the student: ")
        set_student_password(users,roll_number, password)  
        print("Student added successfully.")


def update_student(students,roll_number, name):
    if roll_number in students:
        students[roll_number] = name
        print("Student information updated successfully.")
    else:
        print("Student not found.")
def delete_student(students, attendance_records,roll_number):
    if roll_number in students:
        del students[roll_number]
        del attendance_records[roll_number]
        print("Student deleted successfully.")
    else:
        print("Student not found.")
