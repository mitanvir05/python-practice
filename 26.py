# Write a program to display the multiplication table of a given integer.

num = int(input("Enter an integer: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")