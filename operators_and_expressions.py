# Example 1

a = 10
b = 3

print("Addition:", a + b)  # Addition
print("Subtraction:", a - b)  # Subtraction
print("Multiplication:", a * b)  # Multiplication
print("Division:", a / b)  # Division
print("Modulus:", a % b)  # Modulus
print("Exponentiation:", a**b)  # Exponentiation
print("Floor Division:", a // b)  # Floor Division

# Example 2 - Comparison (Relational) Operators used to compare values and return a boolean value

x = 5
y = 10

print("Equal:", x == y)  # True if x is equal to y
print("Not Equal:", x != y)  # True if x is not equal to y
print("Greater than:", x > y)  # True if x is greater than y
print("Less than:", x < y)  # True if x is less than y
print("Greater than or equal to:", x >= y)  # True if x is greater than or equal to y
print("Less than or equal to:", x <= y)  # True if x is less than or equal to y

# Example 3 - Logical Operators used to combine conditional statements and return a boolean value

p = True
q = False

print("Logical AND:", p and q)  # True if both p and q are True
print("Logical OR:", p or q)  # True if either p or q is True
print("Logical NOT:", not p)  # True if p is False

# Example 4 - Assignment Operators used to assign values to variables

x = 5
x += 2  # Equivalent to x = x + 2
print("Assignment (x += 2):", x)  # x is now 7

y = 10
y -= 3  # Equivalent to y = y - 3
print("Assignment (y -= 3):", y)  # y is now 7

# Example 5 - Bitwise Operators used to perform bit-level operations on integers
a = 60
b = 13

print("Bitwise AND:", a & b)  # Bitwise AND
print("Bitwise OR:", a | b)  # Bitwise OR
print("Bitwise XOR:", a ^ b)  # Bitwise XOR
print("Bitwise NOT:", ~a)  # Bitwise NOT
print("Left Shift:", a << 2)  # Left Shift
print("Right Shift:", a >> 2)  # Right Shift

# Example 6 - Identity Operators used to check if two variables point to the same object in memory
x = ["apple", "banana"]
y = ["apple", "banana"]

z = x
print("Identity (x is z):", x is z)  # True, x and z point to the same object
print("Identity (x is y):", x is y)  # False, x and

# Example 7 - Membership Operators used to check if a value is present in a sequence (list, tuple, set, or string)
my_list = [1, 2, 3, 4, 5]
print("Membership (3 in my_list):", 3 in my_list)  # True
print("Membership (6 in my_list):", 6 in my_list)  # False

# Example 8 - Expressions are combinations of values, variables, operators, and function calls that are evaluated to produce another value

x = 5
y = 3

z = x + y  # Arithmetic expression
print("Expression (x + y):", z)  # Evaluates to 8

is_greater = x > y  # Comparison expression
print("Expression (x > y):", is_greater)  # Evaluates to True

logical_result = (x > 2) and (y < 2)  # Logical expression
print("Expression ((x > 2) and (y < 2)):", logical_result)  # Evaluates to False
