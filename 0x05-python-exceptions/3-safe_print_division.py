#!/usr/bin/python3
def safe_print_division(a, b):
    div = a / b
    try:
        print("{} / {}= {}".format('a', 'b', 'div', end="")
            
    except ZeroDivisionError:
        print("You cannot divide by zero")
        div = None
    finally: 
        print("Inside result: {:d}".format(div))
        return div
