# Write a program to print the sum of digits in a number.

num = int(input("Enter a number: "))

total = 0
while num > 0:
    digit = num % 10
    total += digit
    num //= 10

print(f"Sum of digits: {total}")
