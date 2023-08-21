from login_func import *
from stud_manage import *
from attendance import *

users = {'student1': 'studentpass', 'teacher1': 'teacherpass'}
students = {}
attendance_records = {}

while True:
    print("1. Login")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        username = input("Username: ")
        password = input("Password: ")
        if login(users,username, password):
            print("Login successful.")
            if username in students:
                while True:
                    print("\n1. View My Attendance")
                    print("2. Change Password")
                    print("3. Logout")
                    action = input("Enter your action: ")

                    if action == '1':
                        roll_number = username
                        attendance_data = view_attendance(students, attendance_records,roll_number)
                        for date, present in attendance_data.items():
                            status = "Present" if present else "Absent"
                            print(f"Date: {date}, Status: {status}")

                    elif action == '2':
                        change_student_password(users,username)  

                    elif action == '3':
                        print("Logged out.")
                        break
                    
            elif username.startswith('teacher'):
                while True:
                    print("\n1. Add Student")
                    print("2. Update Student")
                    print("3. Delete Student")
                    print("4. Mark Attendance")
                    print("5. Generate Report (Specific Student)")
                    print("6. Generate Report (All Students)")
                    print("7. Logout")
                    action = input("Enter your action: ")

                    if action == '1':
                        roll_number = input("Enter Roll Number: ")
                        if roll_number in students:
                            print("Roll number already exists.")
                        else:
                            name = input("Enter Name: ")
                            add_student(users,students, attendance_records,roll_number, name)

                    elif action == '2':
                        roll_number = input("Enter Roll Number: ")
                        name = input("Enter Updated Name: ")
                        update_student(students, roll_number, name)

                    elif action == '3':
                        roll_number = input("Enter Roll Number: ")
                        delete_student(students, attendance_records,roll_number)

                    elif action == '4':
                        date_to_mark = input("Enter Date (YYYY-MM-DD): ")
                        mark_attendance(students, attendance_records,date_to_mark)

                    elif action == '5':
                        roll_number = input("Enter Roll Number: ")
                        period = input("Enter Period (daily/weekly/monthly): ")
                        report = generate_report(students, attendance_records,roll_number, period)
                        print(report)

                    elif action == '6':
                        period = input("Enter Period (daily/weekly/monthly): ")
                        generate_all_reports(students,period)
                        
                    elif action == '7':
                        print("Logged out.")
                        break

    elif choice == '2':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please select a valid option.")

