#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    # initialize a counter for the number of integers printed
    count = 0
    # use a try-except block to handle possible errors
    try:
        # loop through the list elements up to x
        for i in range(x):
            # check if the element at index i is an integer
            if isinstance(my_list[i], int):
                # print the element as an integer, followed by a space
                print("{:d}".format(my_list[i]), end=" ")
                # increment the counter by one
                count += 1
        # print a new line after the loop
        print()
    except:
        # if an error occurs, print a new line and pass
        print()
        pass
    # return the number of integers printed
    return count
