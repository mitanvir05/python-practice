# Write a program using python to create a simple calculator.

print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(f"Result: {num1 + num2}")
elif choice == '2':
    print(f"Result: {num1 - num2}")
elif choice == '3':
    print(f"Result: {num1 * num2}")
elif choice == '4':
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid choice")