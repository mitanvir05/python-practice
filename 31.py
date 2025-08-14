# Write a program to determine whether a given number is prime or not.

num = int(input("Enter a number: "))

if num > 1:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a Prime number.")
    else:
        print(f"{num} is not a Prime number.")
else:
    print("Prime numbers are greater than 1.")