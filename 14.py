# A company decided to give bonus to employees based on the following
# conditions:
# 10% of salary if year of service is more than 5 years
# # 5% of salary if year of service is more than 3 years.
# Ask user for their salary and year of service and print the total amount.


salary = float(input("Enter your salary: "))
years = int(input("Enter your years of service: "))

if years > 5:
    bonus = salary * 0.10
elif years > 3:
    bonus = salary * 0.05
else:
    bonus = 0

total_amount = salary + bonus

print(f"Bonus: {bonus}")
print(f"Total amount to be paid: {total_amount}")
