# File: Simple_Calculator
# This program implements a simple calculator that performs basic arithmetic operations:
# addition, subtraction, multiplication, and division.
# It prompts the user to select an operation and input two numbers, then displays the result.   
# It handles invalid inputs and division by zero errors gracefully.

def addition(x, y):     # Function to add two numbers
    return x + y

def subtraction(x, y):      # Function to subtract two numbers
    return x - y

def multiplication(x, y):       # Function to multiply two numbers
    return x * y

def division(x, y):     # Function to divide two numbers
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

def calculator():       # Main function to run the calculator
    result = None

    while True:     # Loop to keep the calculator running until the user chooses to exit
        print("\nSelect Operation:")
        print('1. Addition')
        print('2. Subtraction')
        print('3. Multiplication')
        print('4. Division')
        print('5. Exit')

        choice = input('Enter your choice (1 / 2 / 3 / 4 / 5): ')       # Get user input for the operation choice

        if choice in ('1', '2', '3', '4'):      # Check if the choice is a valid operation
            try:            
                number1 = float(input('Enter first number: '))
                number2 = float(input('Enter second number: '))
            except ValueError:
                print("Invalid input! Please enter numbers.")
                continue

            try:        # Perform the selected operation
                if choice == '1':
                    result = addition(number1, number2)
                elif choice == '2':
                    result = subtraction(number1, number2)
                elif choice == '3':
                    result = multiplication(number1, number2)
                elif choice == '4':
                    result = division(number1, number2)
                print(f'Result: {result}')
            except ZeroDivisionError as e:
                print(f"Error! {e}")

        elif choice == '5':
            print('Exiting calculator... Goodbye!')
            break
        else:
            print('Error! Invalid input, please try again.')

# Run the calculator
calculator()

