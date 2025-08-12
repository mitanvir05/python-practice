# A student will not be allowed to sit in exam if his/her attendance is less than 70%. Take following input from user & print percentage of class attended. Is student is allowed to sit in exam or not?
# Number of classes held
# Number of classes attended.

classes_held = int(input("Enter number of classes held: "))
classes_attended = int(input("Enter number of classes attended: "))

attendance_percentage = (classes_attended / classes_held) * 100

print(f"Attendance Percentage: {attendance_percentage:.2f}%")

if attendance_percentage >= 70:
    print("Allowed to sit in exam.")
else:
    print("Not allowed to sit in exam.")
