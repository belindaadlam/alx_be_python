# pattern_drawing.py

# Prompt the user for the pattern size and convert it to an integer
try:
    size = int(input("Enter the size of the pattern: "))
    if size <= 0:
        print("Please enter a positive integer.")
        exit()
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

# Initialize the row counter for the while loop
row = 0

# Outer while loop controls the number of rows
while row < size:
    # Inner for loop controls the number of columns (asterisks) in the current row
    for col in range(size):
        # Print the asterisk without a newline character at the end
        print("*", end="")
        
    # Print a newline character after the inner loop completes to move to the next line
    print()
    
    # Increment the row counter
    row += 1