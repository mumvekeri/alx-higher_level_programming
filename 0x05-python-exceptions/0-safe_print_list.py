#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # initialize a counter for the number of elements printed
    count = 0
    # use a try-except block to handle possible errors
    try:
        # loop through the list elements up to x
        for i in range(x):
            # print the element at index i, followed by a space
            print(my_list[i], end=" ")
            # increment the counter by one
            count += 1
        # print a new line after the loop
        print()
    except:
        # if an error occurs, print a new line and pass
        print()
        pass
    # return the number of elements printed
    return count
