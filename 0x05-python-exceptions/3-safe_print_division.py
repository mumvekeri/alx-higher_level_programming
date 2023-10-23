#!/usr/bin/python3
def safe_print_division(a, b):
    # initialize a variable to store the result of the division
    result = None
    # use a try-except-finally block to handle possible errors
    try:
        # perform the division and assign the result to the variable
        result = a / b
    except ZeroDivisionError:
        # if a zero division error occurs, print an error message
        print("Division by zero is not allowed")
    finally:
        # print the result of the division preceded by Inside result:
        print("Inside result: {}".format(result))
        # return the result of the division
        return result
