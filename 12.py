# A shop will give discount of 10% if the cost of purchased quantity is morethan 1000.
# Ask user for quantity & per unit price. Print the total cost, discount & amount to pay.

quantity = int(input("Enter quantity: "))
price_per_unit = float(input("Enter price per unit: "))

total_cost = quantity * price_per_unit

if total_cost > 1000:
    discount = total_cost * 0.10
else:
    discount = 0

amount_to_pay = total_cost - discount

print(f"Total cost: {total_cost}")
print(f"Discount: {discount}")
print(f"Amount to pay: {amount_to_pay}")
