# Write a program to return the quotient and remainder of a division.

num1 = int(input("Enter the dividend: "))
num2 = int(input("Enter the divisor: "))

if num2 != 0:
    quotient = num1 // num2
    remainder = num1 % num2
    print(f"Quotient: {quotient}")
    print(f"Remainder: {remainder}")
else:
    print("Error: Division by zero is not allowed.")
