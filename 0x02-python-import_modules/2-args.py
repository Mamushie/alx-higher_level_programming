#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number = len(sys.argv) - 1
    if number == 0:
        print("{:d} arguments.".format(number))
    elif number == 1:
        print("{:d} argument:".format(number))
    else:
        print("{:d} arguments:".format(number))
    if number > 0:
        number = 1
        for arg in sys.argv[1:]:
            number += 1
            print("{:d}: {}".format(number, arg))   
