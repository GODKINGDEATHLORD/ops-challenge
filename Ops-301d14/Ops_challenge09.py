#!/usr/bin/env python3

# Collect two integers from the user
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

# Equals: a == b
if a == b:
    print(f"The numbers are equal: {a} == {b}")

# Not Equals: a != b
if a != b:
    print(f"The numbers are not equal: {a} != {b}")

# Less than: a < b
if a < b:
    print(f"The first number is less than the second number: {a} < {b}")

# Less than or equal to: a <= b
if a <= b:
    print(f"The first number is less than or equal to the second number: {a} <= {b}")

# Greater than: a > b
if a > b:
    print(f"The first number is greater than the second number: {a} > {b}")

# Greater than or equal to: a >= b
if a >= b:
    print(f"The first number is greater than or equal to the second number: {a} >= {b}")

# if statement with elif
if a == b:
    print("a is equal to b")
elif a != b:
    print("a is not equal to b")

# if, elif, else
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")
