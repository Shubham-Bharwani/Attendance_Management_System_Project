
def mark_attendance(students, attendance_records,date):
    for roll_number, name in students.items():
        while True:
            attendance = input(f"Mark attendance for {name} ({roll_number}) [P/A]: ").upper()
            if attendance == 'P':
                attendance_records[roll_number][date] = True
                break
            elif attendance == 'A':
                attendance_records[roll_number][date] = False
                break
            else:
                print("Invalid input. Please enter 'P' for present or 'A' for absent.")

def view_attendance(students, attendance_records,roll_number):
    if roll_number in attendance_records:
        return attendance_records[roll_number]
    return {}


def generate_report(students,attendance_records,roll_number, period):
    attendance_data = attendance_records.get(roll_number, {})
    if period == 'daily':
        latest_date = max(attendance_data.keys()) if attendance_data else None
        if latest_date:
            latest_status = "Present" if attendance_data[latest_date] else "Absent"
            report = f"Latest Daily Attendance Report for {students.get(roll_number, 'Unknown')}:\n"
            report += f"Date: {latest_date}, Status: {latest_status}\n"
        else:
            report = f"No daily attendance recorded for {students.get(roll_number, 'Unknown')}\n"

    elif period == 'weekly':
        latest_dates = sorted(attendance_data.keys(), reverse=True)
        latest_week_dates = latest_dates[:7]
        present_week_days = sum(1 for date in latest_week_dates if attendance_data[date])
        total_week_days = len(latest_week_dates)
        report = f"Weekly Attendance Report for {students.get(roll_number, 'Unknown')}:\n"
        report += f"Present Days: {present_week_days}, Total Days: {total_week_days}\n"
        report += f"Attendance Percentage: {(present_week_days / total_week_days) * 100:.2f}%\n"

    elif period == 'monthly':
        today = input("Enter the current date (YYYY-MM-DD): ")
        year, month, _ = today.split('-')
        last_month = f"{year}-{str(int(month) ).zfill(2)}"

        print("Monthly Attendance Report")
        print("=" * 30)

        # for roll_number, name in students.items():
        month_dates = [date for date in attendance_data.keys() if date.startswith(last_month)]
        if len(month_dates) > 31:
            month_dates = month_dates[-31:]

        present_month_days = sum(1 for date in month_dates if attendance_data[date])
        total_month_days = len(month_dates)

        attendance_percentage = (present_month_days / total_month_days) * 100

        report = f"Roll Number: {roll_number}\n"
        report += f"Student Name: {students[roll_number]}\n"
        report += f"Present Days: {present_month_days}/{total_month_days}\n"
        report += f"Attendance Percentage: {attendance_percentage:.2f}%\n"
        report += "=" * 30
    return report



def generate_all_reports(students,attendance_records,period):
    for roll_number in students:
        report = generate_report(students,attendance_records,roll_number, period)
        print(report)
        print('-' * 30)
