# Write a program to display Fibonacci series up to 10 terms.

n_terms = 10
a, b = 0, 1

print("Fibonacci series up to 10 terms:")
for _ in range(n_terms):
    print(a, end=" ")
    a, b = b, a + b
