# Write a program to find the largest and smallest among three numbers.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

largest = max(a, b, c)
smallest = min(a, b, c)

print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")