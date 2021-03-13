# Program that performs some basic arithmetic calculations.

# Importing math module for Multiplication function.
import math


def addition():
    # Function for adding the numbers that the user is choosing.
    numbers = []
    # Handling errors for wrong quantity input.
    try:
        addition_quantity = int(input("How many numbers would you like to add?: "))
    except ValueError:
        print('Please enter a valid number.')
    else:
        # Handling errors for wrong input for calculations.
        try:
            for i in range(addition_quantity):
                addition_numbers = float(input("Please enter one by one: "))
                numbers.append(addition_numbers)
        except ValueError:
            print('Please enter a valid number.')
        # Displaying result.
        else:
            addition_total = sum(numbers)
            print(f'This is the result: {addition_total}')

    print()
    # Displaying menu again
    program()


def subtraction():
    # Function for subtracting two numbers that the user is choosing.

    # Handling errors for wrong input for calculations.
    try:
        first_number = float(input('Please enter the first number: '))
        second_number = float(input('Please enter the second number: '))
    except ValueError:
        print('Please enter a valid number.')
    # Displaying result.
    else:
        subtraction_total = first_number - second_number
        print(f'This is the result: {subtraction_total}')

    print()
    # Displaying menu again
    program()


def multiplication():
    # Function for multiplying the numbers that the user is choosing.
    numbers = []
    # Handling errors for wrong quantity input.
    try:
        multiplication_quantity = int(input("How many numbers would you like to multiply?: "))
    except ValueError:
        print('Please enter a valid number.')
    else:
        # Handling errors for wrong input for calculations.
        try:
            for i in range(multiplication_quantity):
                multiplication_numbers = float(input("Please enter one by one: "))
                numbers.append(multiplication_numbers)
        except ValueError:
            print('Please enter a valid number.')
        # Displaying result.
        else:
            multiplication_total = math.prod(numbers)
            print(f'This is the result: {multiplication_total}')

    print()
    # Displaying menu again
    program()


def division():
    # Function for dividing two numbers that the user is choosing.

    # Handling errors for wrong input for calculations.
    try:
        first_number = float(input('Please enter the first number: '))
        second_number = float(input('Please enter the second number: '))
    except ValueError:
        print('Please enter a valid number.')
    else:
        # Handling errors for input "0" for calculations.
        if first_number == 0 or second_number == 0:
            print('It is not possible to divide by zero. Please enter a valid number.')
        # Displaying result.
        else:
            division_total = first_number / second_number
            print(f'This is the result: {division_total}')

    print()
    # Displaying menu again
    program()


def program():
    # Function for displaying the menu, so the user can choose an option.
    user_selection = input('Please enter "A" for Addition, "S" for Subtraction, '
                           '"M" for Multiplication, "D" for Division or "E" to exit the program: ').upper()

    if user_selection == 'A':
        addition()
    elif user_selection == 'S':
        subtraction()
    elif user_selection == 'M':
        multiplication()
    elif user_selection == 'D':
        division()
    elif user_selection == 'E':
        user_selection = 'Goodbye! See you next time :)'
        print(user_selection)
    else:
        print('Please enter a valid input.')
        print()
        program()


program()
