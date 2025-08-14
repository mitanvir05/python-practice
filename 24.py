# Write a program to find the sum of all odd numbers from 1 to N.

n = int(input("Enter N: "))

total = 0
for i in range(1, n + 1, 2):
    total += i

print(f"Sum of all odd numbers from 1 to {n} is {total}")