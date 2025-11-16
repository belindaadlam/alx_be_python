# multiplication_table.py

# Prompt the user for a number and convert it to an integer
try:
    number = int(input("Enter a number to see its multiplication table: "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    # Exit if the input is not valid to prevent errors
    exit()

# Use a for loop to iterate through the numbers 1 through 10
# range(1, 11) includes 1 and excludes 11
for i in range(1, 11):
    # Calculate the product of the input number and the current iterator (i)
    product = number * i
    
    # Print the line in the required format
    print(f"{number} * {i} = {product}")