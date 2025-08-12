# A school has following rules for grading system:
# i) Below 50 – F; ii) 50 to 60 – D; iii) 60 to 70 – C; iv) 70 to 80 – B; v) Above 80 – A
# Ask user to enter mark and print the corresponding grade.

marks = float(input("Enter marks: "))

if marks < 50:
    grade = "F"
elif marks < 60:
    grade = "D"
elif marks < 70:
    grade = "C"
elif marks < 80:
    grade = "B"
else:
    grade = "A"

print(f"Grade: {grade}")
