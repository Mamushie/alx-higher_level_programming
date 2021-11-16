#!/usr/bin/python3
def uppercase(str):
    for a in range(len(str)):
        a = ord(str[a])
        if a >= 97 and a <= 122:
            a = a - 32
        print(end="{:c}".format(a))
    print()
