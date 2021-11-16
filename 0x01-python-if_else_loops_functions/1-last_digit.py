#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10
digit = number * -1
print("Last digit of {:d} is ".format(number), end=' ')

if digit > 5:
    print ("{:d} and is greater than 5".format(digit))

elif digit == 0:
    print ("{:d} and is zero".format(digit))

else:
    print ("{:d} and is less than 6 and not 0".format(digit))
