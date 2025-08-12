# Write a program in that takes minutes as input, and display the total number of hours and minutes.

total_minutes = int(input("Enter total minutes: "))

hours = total_minutes // 60
minutes = total_minutes % 60

print(f"{hours} hour(s) and {minutes} minute(s)")
