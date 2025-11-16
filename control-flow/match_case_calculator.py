# match_case_calculator.py

# 1. Prompt for user input and convert numbers to float
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit()

# Prompt for the operation
operation = input("Choose the operation (+, -, *, /): ")

result = None

# 2. Use the match statement to perform the calculation
match operation:
    case '+':
        result = num1 + num2
    
    case '-':
        result = num1 - num2
        
    case '*':
        result = num1 * num2
        
    case '/':
        # Handle division by zero case gracefully
        if num2 != 0:
            result = num1 / num2
        else:
            print("Cannot divide by zero.")
            
    case _:
        # The wildcard (_) catches any case that hasn't been explicitly handled
        print("Invalid operation choice.")

# 3. Output the result if a valid calculation was performed
if result is not None:
    # Using :.2f for clean, standard numerical output
    print(f"The result is {result:.2f}")