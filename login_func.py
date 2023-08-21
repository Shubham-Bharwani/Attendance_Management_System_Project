def login(users,username, password):
    if username in users and users[username] == password:
        return True
    return False

def set_student_password(users,roll_number, password):
    users[roll_number] = password

def change_student_password(users, username):
    old_password = input("Enter your current password: ")
    if username in users and users[username] == old_password:
        new_password = input("Enter your new password: ")
        users[username] = new_password
        print("Password changed successfully.")
    else:
        print("Incorrect old password. Password change failed.")

