# Write a program to find the sum of all even numbers from 1 to N.

n = int(input("Enter N: "))

total = 0
for i in range(2, n + 1, 2):
    total += i

print(f"Sum of all even numbers from 1 to {n} is {total}")