# Write a program to find the avg marks of students in a class using list.

marks = []
n = int(input("Enter number of students: "))

for i in range(n):
    mark = float(input(f"Enter marks of student {i+1}: "))
    marks.append(mark)

average = sum(marks) / n
print(f"Average marks of the class: {average}")
