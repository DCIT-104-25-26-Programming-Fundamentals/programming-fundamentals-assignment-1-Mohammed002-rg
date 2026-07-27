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
