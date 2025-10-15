# task2_math_module.py

# Import the necessary module
import math

# 1. Asks the user for a number as input.
try:
    number = float(input("Enter a number for mathematical calculations: "))
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")
else:
    # 2. Uses the math module to calculate the:
    
    # Square root of the number
    if number >= 0:
        square_root = math.sqrt(number)
    else:
        # math.sqrt will raise a ValueError for negative numbers, handle this.
        square_root = "Undefined (Negative Number)" 
        
    # Natural logarithm (log base e) of the number
    if number > 0:
        natural_log = math.log(number)
    else:
        # math.log will raise a ValueError for non-positive numbers.
        natural_log = "Undefined (Non-positive Number)"

    # Sine of the number (in radians)
    sine_value = math.sin(number)

    # 3. Displays the calculated results.
    print("\n--- Calculation Results ---")
    print(f"Original Number: {number}")
    
    # Format output for better readability
    print(f"Square Root (math.sqrt): {square_root}")
    print(f"Natural Logarithm (math.log): {natural_log}")
    print(f"Sine (math.sin): {sine_value}")
