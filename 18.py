# Write a program to find all odd numbers from 1 to N.

n = int(input("Enter N: "))

for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)