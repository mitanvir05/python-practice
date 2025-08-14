# Write a program to find the sum of first N natural numbers.

n = int(input("Enter N: "))

total = 0
for i in range(1, n + 1):
    total += i

print(f"Sum of first {n} natural numbers: {total}")
