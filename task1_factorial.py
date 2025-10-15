# task1_factorial.py

# 1. Defines a function named factorial that takes a number as an argument
#    and calculates its factorial using a loop.
def factorial(n):
    """
    Calculates the factorial of a non-negative integer n.
    Factorial of 0 is 1.
    """
    # Input validation
    if not isinstance(n, int) or n < 0:
        return "Error: Factorial is only defined for non-negative integers."

    # Factorial of 0 is 1
    if n == 0:
        return 1

    result = 1
    # Use a loop to multiply numbers from 1 up to n
    for i in range(1, n + 1):
        result *= i

    # 2. Returns the calculated factorial.
    return result

# 3. Calls the function with a sample number and prints the output.
sample_number = 5
fact_result = factorial(sample_number)

print(f"The factorial of {sample_number} is: {fact_result}")

# Example call with 0
# print(f"The factorial of 0 is: {factorial(0)}")
