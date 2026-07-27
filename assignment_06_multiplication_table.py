# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_fibonacci(n):
    if n <= 0:
        print("Error: Number of terms must be a positive integer.")
        return
    
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(str(a))
        a, b = b, a + b
    
    print("Fibonacci sequence:", " ".join(sequence))


def is_fibonacci(num):
    if num < 0:
        return False
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num


print("=== PART A: Print First N Fibonacci Terms ===")
n = int(input("How many terms? "))
print_fibonacci(n)

print("\n=== PART B: Check if a Number is Fibonacci ===")
number = int(input("Enter a number to check: "))

if is_fibonacci(number):
    print(f"{number} is a Fibonacci number.")
else:
    print(f"{number} is NOT a Fibonacci number.")
