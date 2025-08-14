# Write a program to read 10 numbers from the keyboard and find their sum and average.

total = 0

for i in range(1, 11):
    num = float(input(f"Enter number {i}: "))
    total += num

average = total / 10

print(f"Sum of the numbers: {total}")
print(f"Average of the numbers: {average}")