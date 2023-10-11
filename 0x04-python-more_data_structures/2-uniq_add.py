#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set()
    total = 0

    for number in my_list:
        if number not in unique_set:
            total += number
            unique_set.add(number)

    return total

# Example usage:
my_list = [1, 2, 2, 3, 3, 4, 5, 5, 5]
result = uniq_add(my_list)
print(result)

