#!/usr/bin/python3
for dig in range(0, 10):
    for digits in range(dig + 1, 10):
        if dig == 8 and digits == 9:
            print("{}{}".format(dig, digits))
        else:
            print("{}{}".format(dig, digits), end=", ")
