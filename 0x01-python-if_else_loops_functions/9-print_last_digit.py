#!/usr/bin/python3
def print_last_digit(num):
    if num < 0:
        num = ((-1) * num) % 10
    else:
        num = num % 10

    print("{:d}".format(num), end="")
    return num
