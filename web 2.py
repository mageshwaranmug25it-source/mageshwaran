def factorial(n):
    """
    Returns the factorial of a non-negative integer.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

try:
    num = int(input("Enter a non-negative integer: "))

    if num < 0:
        print("Error: Factorial is not defined for negative numbers.")
    else:
        print(f"Factorial of {num} is {factorial(num)}")

except ValueError:
    print("Please enter a valid integer.")
