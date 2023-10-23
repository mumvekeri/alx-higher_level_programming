#!/usr/bin/python3
def safe_print_integer(value):
    # use a try-except block to handle possible errors
    try:
        # print the value as an integer, followed by a new line
        print("{:d}".format(value))
        # return True if no error occurs
        return True
    except:
        # return False if an error occurs
        return False
