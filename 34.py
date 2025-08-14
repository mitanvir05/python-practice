# Create a list of marks of ten students.
# Find the largest and smallest mark in the list.
# Find the average mark of the students.
# Sort the marks in ascending order.
# Sort the marks in descending order.
# Remove the smallest mark from the list.
# Insert the average mark at the mid position of the list.
# Create another list of five students’ mark and merge the two lists.


marks = [85, 92, 76, 88, 95, 67, 81, 73, 90, 84]
print("Original marks:", marks)

largest = max(marks)
smallest = min(marks)
print(f"Largest mark: {largest}")
print(f"Smallest mark: {smallest}")

average = sum(marks) / len(marks)
print(f"Average mark: {average}")

marks.sort()
print("Ascending order:", marks)

marks.sort(reverse=True)
print("Descending order:", marks)

marks.remove(min(marks))
print("After removing smallest mark:", marks)

mid_index = len(marks) // 2
marks.insert(mid_index, average)
print("After inserting average at mid position:", marks)

marks2 = [78, 85, 91, 69, 88]
print("Second list:", marks2)

merged_marks = marks + marks2
print("Merged list:", merged_marks)
