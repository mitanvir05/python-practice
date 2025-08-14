# Write a program to check whether a given number is a 'Perfect' number or not. Perfect number, a positive integer that is equal to the sum of its proper divisors. The smallest perfect number is 6, which is the sum of 1, 2, and 3.

num = int(input("Enter a number: "))

if num > 0:
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i

    if sum_of_divisors == num:
        print(f"{num} is a Perfect number.")
    else:
        print(f"{num} is not a Perfect number.")
else:
    print("Please enter a positive integer.")
